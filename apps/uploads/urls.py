from rest_framework.routers import DefaultRouter
from .views import UploadedFileViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("files", UploadedFileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
