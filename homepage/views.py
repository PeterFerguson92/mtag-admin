from rest_framework import status, generics
from rest_framework.response import Response

from .serializers import HomepageSerializer, LeaderSerializer
from .models import Homepage, Leader

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

class LeaderDetailView(generics.GenericAPIView):
    serializer_class = LeaderSerializer
    queryset = Leader.objects.all()

    def get_leader(self, pk):
        try:
            return Leader.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        leader = self.get_leader(pk=pk)
        if leader is None:
            return Response(
                {"status": "fail", "message": f"Leader with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(leader)
        return Response({"status": "success", "result": serializer.data})