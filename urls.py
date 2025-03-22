# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('login/',views.user_login,name='user_login'),
    path('home/',views.home,name='home'),
    path('create_club/', views.create_club, name='create_club'),
    path('create_event/', views.create_event, name='create_event'),
    path('register/<int:event_id>/', views.register_for_event, name='register_for_event'),
    path('events/<str:clubname>/', views.club_events, name='club_events'),
    path('edit_details/', views.edit_details, name='edit_details'),
     path('give_Feedback/<int:event_id>',views.give_Feedback,name='give_Feedback'),
     path('view_Feedback/<int:event_id>',views.view_Feedback,name='view_Feedback'),
]
