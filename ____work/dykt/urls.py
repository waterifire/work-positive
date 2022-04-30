from django.urls import path


from .views import dykt_home, dykt_arena

# urlpatterns below

urlpatterns = [
    path('home/', dykt_home, name='dykt_home'),
    path('quiz/<str:pk>/', dykt_arena, name='dykt_arena'),
]
