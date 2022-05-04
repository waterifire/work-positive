from django.urls import path

from .views import ttma_home

# urlpatterns below

urlpatterns = [
    path('home', ttma_home, name='ttma_home'),
    
]
