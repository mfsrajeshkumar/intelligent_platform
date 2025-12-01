import os
from .celery import app as celery_app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.dev")

__all__ = ["celery_app"]
