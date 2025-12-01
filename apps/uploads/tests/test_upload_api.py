import io
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
def test_file_upload():
    client = APIClient()

    file_content = b"id,name\n1,Test"
    file_obj = io.BytesIO(file_content)
    file_obj.name = "sample.csv"

    response = client.post(
        "/api/uploads/files/",
        {"file": file_obj},
        format="multipart"
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["original_filename"] == "sample.csv"
