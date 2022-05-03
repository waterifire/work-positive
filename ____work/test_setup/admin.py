from django.contrib import admin

from .models import QuizSetup, WordleSetup

# Register your models here.

admin.site.register(QuizSetup)
admin.site.register(WordleSetup)
