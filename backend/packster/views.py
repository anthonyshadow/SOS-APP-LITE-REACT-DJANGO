from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Create your views here.

class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


