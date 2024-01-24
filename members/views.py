from datetime import date, datetime
from activities.models import MONTH
from members.models import Member, Transaction
from rest_framework import status, generics
from rest_framework.response import Response

from .serializers import MemberSerializer, TransactionSerializer

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
            transaction_member = Member.objects.create(name=request_name, surname=request_surname, postcode=request_postcode, house_number=request_house_number )
            data = self.buildData(request, transaction_member)
        else: 
            data = self.buildData(request, members[0])

        return self.createTransaction(data)
        
    
    
    