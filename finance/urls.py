from django.urls import path

from .views import BankAccountView, CreatePaymentIntent, TransactionView, StripeKeyView

urlpatterns = [
    path("stripe-key", StripeKeyView.as_view()),
    path("transaction", TransactionView.as_view()),
    path("bank-account", BankAccountView.as_view()),
    path("create-payment-intent", CreatePaymentIntent.as_view(), name='payment-intent')

]
