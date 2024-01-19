from django.urls import path

from .views import HomepageView, LeaderDetailView

urlpatterns = [
    path("", HomepageView.as_view()),
    path("leader/detail/<uuid:pk>", LeaderDetailView.as_view())

]
