from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import WomenModel
from .serializer import WomenSerializer
# Create your views here.
class WomenListView(generics.ListCreateAPIView):
    queryset=WomenModel.objects.all()
    serializer_class=WomenSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )

class WomenDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WomenModel.objects.all()
    serializer_class = WomenSerializer
    lookup_field = 'id'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    