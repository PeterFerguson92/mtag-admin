from django.urls import path

from .views import (
    MinistryView,
    MinistryDetailView,
)

urlpatterns = [
    path("", MinistryView.as_view()),
    path("detail/<uuid:pk>", MinistryDetailView.as_view())
]