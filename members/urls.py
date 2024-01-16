from django.urls import path

from .views import MemberView

urlpatterns = [
    path("", MemberView.as_view()),
]
