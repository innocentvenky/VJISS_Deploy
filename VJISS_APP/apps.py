from django.apps import AppConfig
import os

class VjissAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "VJISS_APP"

    def ready(self):
        if os.environ.get("RENDER"):  # prevents local execution
            from .bootstrap import bootstrap_admin_user
            bootstrap_admin_user()
