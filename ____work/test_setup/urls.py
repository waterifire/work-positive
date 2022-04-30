from django.urls import path


from .views import ts_home, ts_quiz

# urlpatterns below

urlpatterns = [
    path('home/', ts_home, name='ts_home'),
    path('setup_quiz/', ts_quiz, name='ts_quiz'),
]
