from rest_framework import serializers
from .models import User

class PacksterSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields = ('id', 'name', 'password', 'email', 'age')