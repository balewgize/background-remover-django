from io import BytesIO
import os

from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from rembg import remove
import requests
from requests.adapters import Retry, HTTPAdapter

from .models import UserActivity


session = requests.Session()  # to retry failed requests (3 times)
retries = Retry(total=3, backoff_factor=1)
session.mount("http://", HTTPAdapter(max_retries=retries))
session.mount("https://", HTTPAdapter(max_retries=retries))


@receiver(post_save, sender=UserActivity)
def process_image(sender, instance, *args, **kwargs):
    """Process user uploaded image and remove its background."""
    if instance.result:
        return

    environment = os.getenv("DJANGO_SETTINGS_MODULE")
    if "production" in environment:
        # get image from Dropbox when in production
        response = session.get(instance.image.url)
        if response.status_code != 200:
            return
        image_file = Image.open(BytesIO(response.content))
    else:
        # get image from disk when in local
        image_file = Image.open(instance.image.path)

    path, ext = instance.image.name.split(".")
    filename = path.split("/")[-1]
    result_path = f"{filename}_output.{ext}"

    output = remove(image_file)  # remove background using rembg
    output.convert("RGB")
    output.save(result_path, "PNG")

    instance.result.save(result_path, File(open(result_path, "rb")))
    os.remove(result_path)
