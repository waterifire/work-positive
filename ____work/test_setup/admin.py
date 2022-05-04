from django.contrib import admin

from .models import QuizSetup, WordleSetup, TtmaSetup

# Register your models here.

admin.site.register(QuizSetup)
admin.site.register(WordleSetup)
admin.site.register(TtmaSetup)
