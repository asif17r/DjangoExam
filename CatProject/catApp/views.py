from django.shortcuts import render
from rest_framework import generics
from .models import CatShop
from .serializers import CatSerializer

# Create your views here.
class ListCat(generics.ListCreateAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatSerializer

class DetailCat(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatSerializer

