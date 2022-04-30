from django import forms

from .models import Hobby, HobbyList

# forms below

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['hobby_user', 'hobby_name']


class HobbyListForm(forms.ModelForm):
    class Meta:
        model = HobbyList
        fields = ['hobbylist_name']
