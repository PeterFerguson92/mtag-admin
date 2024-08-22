from datetime import date
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import MemberSerializer

# Create your views here.
class MemberView(generics.GenericAPIView):
     def post(self, request, *args, **kwargs):

        data = {
            'name': request.data.get('name'), 
            'middle_name': request.data.get('middleName'), 
            'surname': request.data.get('surname'),
            'email': request.data.get('email'),  
            'postcode': request.data.get('postcode'),
            'house_number': request.data.get('house_number'),
            'address': request.data.get('address'),
            'telephone': request.data.get('phone'), 
            'sex': request.data.get('sex'), 
            'member_type': request.data.get('memberType'),
            'department': request.data.get('department'),
            'origin': request.data.get('origin'), 
            'membership_start': date.today()        
        }
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)