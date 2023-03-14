from django.contrib import admin

from .models import UserActivity


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ["slug", "image", "result", "created_at"]
