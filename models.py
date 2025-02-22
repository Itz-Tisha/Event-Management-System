from django.db import models

# Create your models here.
class UserType(models.Model):
    USER_TYPES = [
        ('organizer', 'Organizer'),
        ('participant', 'Participant'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)  
    password = models.CharField(max_length=255) 
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return f"{self.name} ({self.get_user_type_display()})"
    

class club(models.Model):
    clubname=models.CharField(max_length=20,unique=True)
    desc = models.CharField(max_length=50)
    org_name = models.ForeignKey(UserType,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.clubname} (Organizer: {self.org_name})"
    
class event(models.Model):
    event_name = models.CharField(max_length=20,unique=True)
    location = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    desc = models.CharField(max_length=50)
    club_name = models.ForeignKey(club,on_delete=models.CASCADE)


class event_reg(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20,unique=True)
    event_name = models.ForeignKey(event,on_delete=models.CASCADE)

