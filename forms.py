
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserType,event_reg,club,event,feedback
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserType
        fields = ['name', 'email', 'password', 'user_type']

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password and len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return make_password(password)  

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        

        return cleaned_data



from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password"
    )
 

class ClubForm(forms.ModelForm):
    class Meta:
        model = club  
        fields = ['clubname', 'desc']
        widgets = {
            'clubname': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
           
        }


    def clean_clubname(self):  
        name = self.cleaned_data.get('clubname')
        if club.objects.filter(clubname=name).exists():
            raise forms.ValidationError('Club already exists')
        return name  



class eventform(forms.ModelForm):
    class Meta:
        model = event
        fields = ['event_name', 'location', 'start_time', 'end_time', 'date', 'desc', 'club_name']
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Textarea(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'club_name': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        clubs = kwargs.pop('clubs', club.objects.none()) 
        super().__init__(*args, **kwargs)
        
    
        self.fields['club_name'].queryset = clubs



class EventRegForm(forms.ModelForm):
    class Meta:
        model = event_reg
        fields = ['name', 'email']  

class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['name' , 'feedback']
    
    def __str__(self):
        return f"Feedback by {self.name} for {self.event_name.event_name}"
