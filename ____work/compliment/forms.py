from django.forms import ModelForm

from .models import Compliment

# forms below

class ComplimentForm(ModelForm):
    class Meta:
        model = Compliment
        fields = ['description']
