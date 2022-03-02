from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PacksterSerializer
from .models import User

# Create your views here.

class PacksterView(viewsets.ModelViewSet):
    serializer_class = PacksterSerializer
    queryset = User.objects.all()
