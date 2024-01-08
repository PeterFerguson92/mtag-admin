from rest_framework import serializers

from .models import Weekly, Event, Monthly


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class WeeklySerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Weekly
        fields = "__all__"


class MonthlySerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Monthly
        fields = "__all__"
