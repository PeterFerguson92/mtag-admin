from django.urls import path

from .views import (
    MinistryView,
    MinistryDetailView,
)

urlpatterns = [
    path("", MinistryView.as_view()),
    path("ministry/<uuid:pk>", MinistryDetailView.as_view())
]