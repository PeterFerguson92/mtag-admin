from rest_framework import status, generics
from rest_framework.response import Response

from .serializers import HomepageSerializer
from .models import Homepage

class HomepageView(generics.GenericAPIView):
    serializer_class = HomepageSerializer

    def get(self, request):
        objects = Homepage.objects.all()
        if not objects:
            return Response(
                {"status": "No homepage data available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(objects, many=True)
        return Response({"status": "success", "result": serializer.data})