from datetime import date, datetime
from django.shortcuts import render
from constants import MONTH
from finance.models import BankAccount
from finance.serializers import BankAccountSerializer, TransactionSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from mtag_admin.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY
import stripe

from servicemanagement.models import Member

stripe.api_key=STRIPE_SECRET_KEY

# Create your views here.
class StripeKeyView(generics.GenericAPIView):
    
    def get(self, request):
        stripe_api_key = STRIPE_PUBLISHABLE_KEY
        if not stripe_api_key:
            return Response(
                {"status": "No stripe key found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response({"status": "success", 'key': STRIPE_PUBLISHABLE_KEY}, status=200)

class BankAccountView(generics.GenericAPIView):
    serializer_class = BankAccountSerializer

    def get(self, request):
        accounts = BankAccount.objects.filter(visible=True)
        if not accounts:
            return Response(
                {"status": "No accounts available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(accounts, many=True)
        return Response({"status": "success", "result": serializer.data})
    
class TransactionView(generics.GenericAPIView):
    
     def buildData(self, request, member):
        currentDate = date.today()        
        currentMonthIndex = datetime.now().month
        currentMonth = MONTH[currentMonthIndex - 1][0]
        return {
            'amount': request.data.get('amount'), 
            'type': request.data.get('type'), 
            'specific_transaction_type': request.data.get('specificTransactionType'), 
            'member': member.id, 
            'source': request.data.get('source'), 
            'message': request.data.get('message'),
            "opted_in_gift_aid_donation": request.data.get('optedInGiftAidDonation'),
            "gift_aid_donation_occurence": request.data.get('giftAidDonationOccurence'),
            'date': currentDate, 
            'month': currentMonth, 
        }
    
     def createTransaction(self, data):
         serializer = TransactionSerializer(data=data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
     def post(self, request, *args, **kwargs):
        request_name = request.data.get('name')
        request_surname = request.data.get('surname')
        request_postcode = request.data.get('postcode')
        request_house_number = request.data.get('houseNumber')
        member_type = request.data.get('memberType')
        members = Member.objects.filter(name=request_name).filter(surname=request_surname).filter(postcode=request_postcode).filter(house_number=request_house_number)
        data = None
        if members.count() == 0:
            transaction_member = Member.objects.create(name=request_name, surname=request_surname, postcode=request_postcode, 
                                                       house_number=request_house_number, origin='WEBSITE',member_type=member_type)
            data = self.buildData(request, transaction_member)
        else: 
            data = self.buildData(request, members[0])

        return self.createTransaction(data)

class CreatePaymentIntent(generics.GenericAPIView):
     def post(self, request,*args, **kwargs):
        try:
            intent=stripe.PaymentIntent.create(
               amount=int(request.data.get('amount')) * 100,
               currency='usd',
               automatic_payment_methods={
                'enabled': True,
                },
                metadata={
                    'transaction_type':request.data.get('type')
                } 
            )
            return Response({'client_secret':intent['client_secret'], 'key': STRIPE_PUBLISHABLE_KEY}, status=200)
        
        except Exception as e:
            return Response({'error':str(e)}, status=400)