from django import forms

from .models import Bio

# forms below

class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ['name', 'email', 'password',
                'job_title', 'job_description',
                'like1', 'like2', 'like3', 'like4',
                'hobby1', 'hobby2', 'hobby3', 'hobby4',]

