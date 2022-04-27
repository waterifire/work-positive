from django.urls import path


from .views import compliment_home, compliment_user

# urlpatterns below

urlpatterns = [
    path('home/', compliment_home, name='compliment_home'),
    path('user/<str:pk>/', compliment_user, name='compliment_user'),
]
