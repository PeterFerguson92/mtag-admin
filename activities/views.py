from rest_framework import status, generics
from rest_framework.response import Response

from .serializers import EventSerializer, WeeklySerializer
from .models import Event, Weekly


class EventView(generics.GenericAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get(self, request):
        events = Event.objects.all()
        if not events:
            return Response(
                {"status": "No Events available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(events, many=True)
        return Response({"status": "success", "result": serializer.data})

class EventDetailView(generics.GenericAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_event(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        event = self.get_event(pk=pk)
        if event is None:
            return Response(
                {"status": "fail", "message": f"Event with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(event)
        return Response({"status": "success", "result": serializer.data})


class WeeklyView(generics.GenericAPIView):
    serializer_class = WeeklySerializer
    queryset = Weekly.objects.all()

    def get(self, request):
        objects = Weekly.objects.all()
        if not objects:
            return Response(
                {"status": "No weekly data available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(objects, many=True)
        return Response({"status": "success", "result": serializer.data})