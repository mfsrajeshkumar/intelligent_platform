import io
import pytest
from rest_framework.test import APIClient
from apps.uploads.models import UploadedFile, UploadStatus
from apps.uploads.tasks import process_uploaded_file


@pytest.mark.django_db
def test_celery_process_uploaded_file():
    client = APIClient()

    file = io.BytesIO(b"id,name\n1,A")
    file.name = "test.csv"

    response = client.post("/api/uploads/files/", {"file": file}, format="multipart")
    file_id = response.data["id"]

    # call celery task synchronously
    process_uploaded_file(file_id)

    obj = UploadedFile.objects.get(id=file_id)
    assert obj.status == UploadStatus.COMPLETED
