from django.urls import path

from .views import MemberView, TransactionView

urlpatterns = [
    path("", MemberView.as_view()),
    path("transaction", TransactionView.as_view()),
]
