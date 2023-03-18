from datetime import datetime
from uuid import uuid4

from django.db import models
from django.urls import reverse


def get_upload_path(instance, filename):
    """Return timestamp filename for user uploaded files."""

    ext = filename.split(".")[-1]
    time_stamp = datetime.today().strftime("%Y%m%d_%H%M%S")
    folder = datetime.today().strftime("%Y/%m")
    image_path = f"{folder}/{time_stamp}.{ext}"
    return image_path


class UserActivity(models.Model):
    """
    A class representing user activity

    Uploading image to remove its background and downloading.
    """

    image = models.ImageField(upload_to=get_upload_path)
    result = models.ImageField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=uuid4)

    class Meta:
        verbose_name = "User Activity"
        verbose_name_plural = "User Activities"

    def __str__(self) -> str:
        return str(self.slug)

    def get_absolute_url(self):
        return reverse("bgremove:result", args=(self.slug,))
