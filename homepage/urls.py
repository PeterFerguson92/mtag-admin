from django.urls import path

from .views import AboutUsDetailView, HomepageView, LeaderDetailView

urlpatterns = [
    path("", HomepageView.as_view()),
    path("leader/detail/<uuid:pk>", LeaderDetailView.as_view()),
    path("aboutus/detail", AboutUsDetailView.as_view())

]
