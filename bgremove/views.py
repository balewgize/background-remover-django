from django.views.generic import CreateView, DetailView

from .models import UserActivity


class UploadView(CreateView):
    model = UserActivity
    fields = ["image"]
    template_name = "index.html"


class ResultView(DetailView):
    model = UserActivity
    template_name = "result.html"
    context_object_name = "user_activity"
