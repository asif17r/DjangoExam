from django.shortcuts import render
from rest_framework import generics
from .models import CatShop
from .serializers import CatSerializer

from django.contrib.auth.mixins import LoginRequiredMixin

# class MyProtectedView(LoginRequiredMixin, View):
#     # Your view logic here
#     def get(self,request, format=None):
#         return Response({
#             'status': 'Congratutations! You are authenticated!'
#         })

# Create your views here.
class ListCat(generics.ListCreateAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatSerializer

class DetailCat(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatSerializer

