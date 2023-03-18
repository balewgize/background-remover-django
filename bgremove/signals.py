import os

from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from rembg import remove

from .models import UserActivity


@receiver(post_save, sender=UserActivity)
def process_image(sender, instance, *args, **kwargs):
    """Process user uploaded image and remove its background."""

    if not instance.result:
        image_path = instance.image.path

        name, ext = image_path.split(".")
        result_path = f"{name}_output.{ext}"

        input = Image.open(image_path)
        output = remove(input)  # remove background using rembg
        output.convert("RGB")
        output.save(result_path, "PNG")

        instance.result.save(result_path, File(open(result_path, "rb")))
        os.remove(result_path)
