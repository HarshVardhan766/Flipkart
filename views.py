from django.shortcuts import render
from rest_framework import status
from django.shortcuts import APIView
from django.shortcuts import Response
from Customer.models import*
from django.shortcuts import*
# Create your views here.
class GetcustomerView(APIView):
    def get(self,request):
        instance = Customer.objects.all()
serializers=Getcustomerserializers(instance,many=True)
return Response (serializers.data)