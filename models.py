from django.db import models
from django.contrib.auth.hashers import make_password, check_password


 
class participants(models.Model):
    name=models.CharField(max_length=10)
    email=models.CharField(max_length=20) 
    password=models.CharField(max_length=8)



class organizer(models.Model):
    name=models.CharField(max_length=10)
    email=models.CharField(max_length=20) 
    password=models.CharField(max_length=8)
