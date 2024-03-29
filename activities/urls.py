from django.urls import path

from .views import (
    EventView,
    EventDetailView,
    SocialEventDetailView,
    SocialEventView,
    WeeklyView,
    ProgramView,
    ProgramDetailView,
    ProgramActiveView
)

urlpatterns = [
    path("events", EventView.as_view()),
    path("event/<uuid:pk>", EventDetailView.as_view()),
    path("socialevent", SocialEventView.as_view()),
    path("socialevent/<uuid:pk>", SocialEventDetailView.as_view()),
    path("weekly", WeeklyView.as_view()),
    path("program", ProgramView.as_view()),
    path("program/<uuid:pk>", ProgramDetailView.as_view()),
    path("program/active", ProgramActiveView.as_view()),

]
