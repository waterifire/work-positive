from django.urls import path


from .views import enter_gate

# urlpatterns below

urlpatterns = [
        path('enter_gate/', enter_gate, name='enter_gate'),
        ]
