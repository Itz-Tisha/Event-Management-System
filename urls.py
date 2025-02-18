
from django.urls import path, include
from . import views

urlpatterns = [
   path("",views.SignupPage,name="SignupPage"),
   path("login/",views.LoginPage,name="LoginPage"),
   path("home/",views.HomePage,name="HomePage"),
   path("logoutv/",views.logoutv,name="logoutv"),
   path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('createeventform/',views.createeventform,name="createeventform")
]
