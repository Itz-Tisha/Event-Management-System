from django.contrib import admin
from . models import UserType,club,event,event_reg,feedback
admin.site.register(UserType)
admin.site.register(club)
admin.site.register(event)
admin.site.register(event_reg)
admin.site.register(feedback)
