from datetime import date, datetime
from activities.models import MONTH
from members.models import Member, Transaction
from mtag_admin.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY
from rest_framework import status, generics
from rest_framework.response import Response
import stripe
from .serializers import MemberSerializer, TransactionSerializer

stripe.api_key=STRIPE_SECRET_KEY

class StripeKeyView(generics.GenericAPIView):
    
    def get(self, request):
        stripe_api_key = STRIPE_PUBLISHABLE_KEY
        if not stripe_api_key:
            return Response(
                {"status": "No stripe key found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response({"status": "success", 'key': STRIPE_PUBLISHABLE_KEY}, status=200)

class MemberView(generics.GenericAPIView):
     def post(self, request, *args, **kwargs):

        data = {
            'name': request.data.get('name'), 
            'middle_name': request.data.get('middleName'), 
            'surname': request.data.get('surname'), 
            'telephone': request.data.get('phone'), 
            'sex': request.data.get('sex'), 
            'member_type': request.data.get('memberType'), 
            'origin': request.data.get('origin') 
        }
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TransactionView(generics.GenericAPIView):
    
     def buildData(self, request, member):
        currentDate = date.today()        
        currentMonthIndex = datetime.now().month
        currentMonth = MONTH[currentMonthIndex - 1][0]
        return {
            'amount': request.data.get('amount'), 
            'type': request.data.get('type'), 
            'member': member.id, 
            'source': request.data.get('source'), 
            'message': request.data.get('message'), 
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
        members = Member.objects.filter(name=request_name).filter(surname=request_surname).filter(postcode=request_postcode).filter(house_number=request_house_number)
        data = None
        if members.count() == 0:
            transaction_member = Member.objects.create(name=request_name, surname=request_surname, postcode=request_postcode, 
                                                       house_number=request_house_number, origin='WEBSITE' )
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