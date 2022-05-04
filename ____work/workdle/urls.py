from django.urls import path

from .views import workdle_home, workdle_arena

# urlpatterns below

urlpatterns = [
    path('home/', workdle_home, name='workdle_home'),
    path('arena/<str:pk>/', workdle_arena, name='workdle_arena')
]
