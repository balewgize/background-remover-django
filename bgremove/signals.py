import io
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

    response = session.get(instance.image.url)
    if response.status_code != 200:
        return

    path, ext = instance.image.name.split(".")
    filename = path.split("/")[-1]
    result_path = f"{filename}_output.{ext}"

    input = Image.open(io.BytesIO(response.content))
    output = remove(input)  # remove background using rembg
    output.convert("RGB")
    output.save(result_path, "PNG")

    instance.result.save(result_path, File(open(result_path, "rb")))
    os.remove(result_path)
