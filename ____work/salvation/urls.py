from django.urls import path

from .views import salvation_home

# urlpatterns below

urlpatterns = [
    path('home/', salvation_home, name='salvation_home'),
]
