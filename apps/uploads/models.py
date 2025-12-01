import os
import uuid
from pathlib import Path

from django.conf import settings
from django.db import models
from django.utils import timezone


class UploadStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    PROCESSING = "PROCESSING", "Processing"
    COMPLETED = "COMPLETED", "Completed"
    FAILED = "FAILED", "Failed"


def upload_to(instance, filename):
    today = timezone.now().date()
    safe_filename = Path(filename).name.replace(" ", "_")
    return os.path.join(
        "uploads",
        "raw",
        str(today.year),
        f"{today.month:02d}",
        f"{today.day:02d}",
        f"{uuid.uuid4()}__{safe_filename}",
    )


class UploadedFile(models.Model):
    original_filename = models.CharField(max_length=255)
    stored_file = models.FileField(upload_to=upload_to)
    file_size = models.BigIntegerField()
    content_type = models.CharField(max_length=100, blank=True)
    checksum = models.CharField(max_length=64, blank=True)

    status = models.CharField(
        max_length=20,
        choices=UploadStatus.choices,
        default=UploadStatus.PENDING,
    )

    error_message = models.TextField(blank=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        db_table = "uploaded_files"

    def __str__(self):
        return f"{self.original_filename} ({self.status})"
