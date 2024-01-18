from rest_framework import status, generics
from rest_framework.response import Response
from datetime import datetime, date

from .serializers import EventSerializer, WeeklySerializer, ProgramSerializer
from .models import Event, Program, Weekly

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

class ProgramView(generics.GenericAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

    def get(self, request):
        program = Program.objects.all()
        if not program:
            return Response(
                {"status": "No Program available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(program, many=True)
        return Response({"status": "success", "result": serializer.data})

class ProgramActiveView(generics.GenericAPIView):
    serializer_class = ProgramSerializer
    
    def get_active_programs(self):
        try:
            current_date = date.today()
            print(current_date)
            return Program.objects.filter(start_date__gte=current_date)
        except:
            return None
    
    def get(self, request):
        programs = self.get_active_programs()
        if not programs:
            return Response(
                {"status": "No Active Program available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(programs, many=True)
        return Response({"status": "success", "result": serializer.data})
    
class ProgramDetailView(generics.GenericAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

    def get_program(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        program = self.get_program(pk=pk)
        if program is None:
            return Response(
                {"status": "fail", "message": f"Program with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(program)
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