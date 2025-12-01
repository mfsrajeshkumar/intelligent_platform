from rest_framework.response import Response
from rest_framework.views import APIView

import logging
logger = logging.getLogger("app")



class HealthCheckAPIView(APIView):
    def get(self, request):
        # logger.info("File uploaded successfully.")
        return Response({"status": "ok", "message": "Service running"})
