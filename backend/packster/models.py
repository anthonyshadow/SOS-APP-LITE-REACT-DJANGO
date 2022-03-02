import email
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=20)
    age = models.CharField(max_length=3)

    def __str__(self): 
        return self.name, self.email, self.age