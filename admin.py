from django.contrib import admin
from .models import participants
from .models import organizer,gdg
# Register your models here.
admin.site.register(participants)
admin.site.register(organizer)
admin.site.register(gdg)
