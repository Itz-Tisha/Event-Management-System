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
     
class gdg(models.Model):
    event_name=models.CharField(max_length=20)
    location=models.CharField(max_length=30)
    date=models.DateField()
    starttime=models.TimeField()
    endtime=models.TimeField()
    desc=models.CharField(max_length=50)
    purpose_of_even=models.CharField(max_length=50)
    event_img=models.ImageField()
    conact=models.IntegerField()
