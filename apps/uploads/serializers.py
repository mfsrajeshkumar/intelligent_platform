from rest_framework import serializers
from .models import UploadedFile, UploadStatus


class UploadedFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)

    class Meta:
        model = UploadedFile
        fields = [
            "id",
            "file",
            "original_filename",
            "file_size",
            "content_type",
            "status",
            "error_message",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "original_filename",
            "file_size",
            "content_type",
            "status",
            "error_message",
            "created_at",
        ]

    def validate_file(self, file):
        max_size = 50 * 1024 * 1024  # 50 MB
        if file.size > max_size:
            raise serializers.ValidationError("File exceeds size limit (50MB).")
        return file

    def create(self, validated_data):
        request = self.context.get("request")
        file = validated_data.pop("file")

        instance = UploadedFile.objects.create(
            original_filename=file.name,
            stored_file=file,
            file_size=file.size,
            content_type=getattr(file, "content_type", ""),
            uploaded_by=request.user if request and request.user.is_authenticated else None,
        )
        return instance
