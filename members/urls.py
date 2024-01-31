from django.urls import path

from .views import CreatePaymentIntent, MemberView, TransactionView, StripeKeyView

urlpatterns = [
    path("", MemberView.as_view()),
    path("stripe-key", StripeKeyView.as_view()),
    path("transaction", TransactionView.as_view()),
    path("create-payment-intent", CreatePaymentIntent.as_view(), name='payment-intent')

]
