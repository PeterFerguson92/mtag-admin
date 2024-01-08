from django.urls import path

from .views import EventView, WeeklyView

urlpatterns = [
    path("events", EventView.as_view()),
    path("weekly", WeeklyView.as_view()),
]
