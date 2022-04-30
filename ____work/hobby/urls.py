from django.urls import path


from .views import hobby_home, hobby_area

# Urlpatterns

urlpatterns = [
    path('home/', hobby_home , name='hobby_home'),
    path('area/<str:pk>/', hobby_area, name='hobby_area'),
]
