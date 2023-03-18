from django.apps import AppConfig


class BgremoveConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bgremove"

    def ready(self) -> None:
        from . import signals
