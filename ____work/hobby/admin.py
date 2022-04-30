from django.contrib import admin

from .models import Hobby, HobbyList

# Register your models here.

admin.site.register(Hobby)
admin.site.register(HobbyList)
