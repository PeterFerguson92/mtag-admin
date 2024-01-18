from django.urls import path

from .views import EventView, EventDetailView, WeeklyView

urlpatterns = [
    path("events", EventView.as_view()),
    path("weekly", WeeklyView.as_view()),
    path("event/<uuid:pk>", EventDetailView.as_view()),
]
