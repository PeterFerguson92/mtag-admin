from rest_framework import status, generics
from rest_framework.response import Response

from .serializers import AboutUsSerializer, HomepageSerializer, LeaderSerializer, LeadershipBoardSerializer
from .models import AboutUs, Homepage, Leader, LeadershipBoard

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
    

class AboutUsDetailView(generics.GenericAPIView):
    serializer_class = AboutUsSerializer

    def get(self, request):
        objects = AboutUs.objects.all()
        if not objects:
            return Response(
                {"status": "No about us data available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(objects, many=True)
        return Response({"status": "success", "result": serializer.data})
    
class LeadershipBoardView(generics.GenericAPIView):
    serializer_class = LeadershipBoardSerializer

    def get(self, request):
        objects = LeadershipBoard.objects.all()
        if not objects:
            return Response(
                {"status": "No Leadership Board data available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(objects, many=True)
        return Response({"status": "success", "result": serializer.data})

class LeaderDetailView(generics.GenericAPIView):
    serializer_class = LeaderSerializer

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