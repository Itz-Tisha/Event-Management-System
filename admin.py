from django.contrib import admin
from .models import participants
from .models import organizer
# Register your models here.
admin.site.register(participants)
admin.site.register(organizer)