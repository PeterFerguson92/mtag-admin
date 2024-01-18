from ministries.models import Ministry
from rest_framework import status, generics
from rest_framework.response import Response

from .serializers import MinistrySerializer

# Create your views here.
class MinistryView(generics.GenericAPIView):
    serializer_class = MinistrySerializer
    queryset = Ministry.objects.all()

    def get(self, request):
        events = Ministry.objects.all()
        if not events:
            return Response(
                {"status": "No Ministry available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(events, many=True)
        return Response({"status": "success", "result": serializer.data})

class MinistryDetailView(generics.GenericAPIView):
    serializer_class = MinistrySerializer
    queryset = Ministry.objects.all()

    def get_event(self, pk):
        try:
            return Ministry.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        event = self.get_event(pk=pk)
        if event is None:
            return Response(
                {"status": "fail", "message": f"Ministry with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(event)
        return Response({"status": "success", "result": serializer.data})