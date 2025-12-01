import logging
from rest_framework import viewsets, permissions, parsers
from .models import UploadedFile
from .serializers import UploadedFileSerializer

from .tasks import process_uploaded_file

logger = logging.getLogger("app")


class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     logger.info(f"File uploaded: {instance.original_filename}")


    def perform_create(self, serializer):
        instance = serializer.save()

        # Trigger Celery async task
        process_uploaded_file.delay(instance.id)
        logger.info(f"Triggered Celery task for file: {instance.id}")

