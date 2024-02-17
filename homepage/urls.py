from django.urls import path

from .views import AboutUsDetailView, BroadcastView, HomepageView, LeaderDetailView, LeadershipBoardView, DetailsView, SocialMediaView

urlpatterns = [
    path("", HomepageView.as_view()),
    path("leadershipBoard", LeadershipBoardView.as_view()),
    path("leader/detail/<uuid:pk>", LeaderDetailView.as_view()),
    path("aboutus/detail", AboutUsDetailView.as_view()),
    path("details", DetailsView.as_view()),
    path("broadcast", BroadcastView.as_view()),
    path("socialmedia", SocialMediaView.as_view())
]
