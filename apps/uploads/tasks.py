import logging
import time
import pandas as pd
from celery import shared_task
from django.db import transaction

from .models import UploadedFile, UploadStatus

logger = logging.getLogger("app")


@shared_task(bind=True, max_retries=3)
def process_uploaded_file(self, uploaded_file_id):
    """
    Background Celery task that processes uploaded files.
    """
    logger.info(f"Starting file processing | File ID: {uploaded_file_id}")

    try:
        file_obj = UploadedFile.objects.get(id=uploaded_file_id)

        # Update status → PROCESSING
        file_obj.status = UploadStatus.PROCESSING
        file_obj.save(update_fields=["status"])

        # Simulate heavy processing
        time.sleep(2)

        # Parse file (CSV, XLSX)
        file_path = file_obj.stored_file.path
        df = pd.read_csv(file_path) if file_path.endswith(".csv") else None

        # (Later: push results to DB, generate reports, etc.)

        # Mark as completed
        file_obj.status = UploadStatus.COMPLETED
        file_obj.save(update_fields=["status"])

        logger.info(f"File processing completed | File ID: {uploaded_file_id}")
        return True

    except Exception as e:
        logger.error(f"Error processing file: {e}")

        # Mark as failed
        file_obj = UploadedFile.objects.get(id=uploaded_file_id)
        file_obj.status = UploadStatus.FAILED
        file_obj.error_message = str(e)
        file_obj.save(update_fields=["status", "error_message"])

        # Retry with backoff
        raise self.retry(exc=e, countdown=5)
