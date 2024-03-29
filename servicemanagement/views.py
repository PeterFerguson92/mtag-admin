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