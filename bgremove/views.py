import os
from typing import Dict, Any

from django.http import HttpResponse
from django.shortcuts import render
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.generic import CreateView, DetailView
from rembg import remove
from PIL import Image

from .models import UserActivity


class UploadView(CreateView):
    model = UserActivity
    fields = ["image"]
    template_name = "index.html"


class ResultView(DetailView):
    model = UserActivity
    template_name = "result.html"
    context_object_name = "activity"

    def get(self, request, *args: Any, **kwargs: Any) -> HttpResponse:
        activity = self.get_object()
        if not activity.result:
            image_path = activity.image.path
            name, ext = image_path.split(".")
            result_path = f"{name}_output.{ext}"

            input = Image.open(image_path)
            output = remove(input)  # remove background using rembg
            output.convert("RGB")
            output.save(result_path, "PNG")

            activity.result.save(result_path, File(open(result_path, "rb")))
            os.remove(result_path)

        context = {"activity": activity}
        return render(request, self.template_name, context)
