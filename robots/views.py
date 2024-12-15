import datetime

from django.core.files import File
from django.http import FileResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from robots.serializers import RobotSerializer
from services.robots import DownloadRobots


# Create your views here.
class RobotCreateView(APIView):
    serializer_class = RobotSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DownloadRobotsInfoView(APIView):

    def get(self, request):
        temp = DownloadRobots().render_excel_file()
        data = File(temp)
        response = FileResponse(
            data,
            as_attachment=True,
            filename=f"report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
        return response
