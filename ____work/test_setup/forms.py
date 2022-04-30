from django import forms

from .models import QuizSetup

# forms below

class QuizSetupForm(forms.ModelForm):
    class Meta:
        model = QuizSetup
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',]
        
