from django import forms

from .models import QuizSetup, WordleSetup, TtmaSetup

# forms below

class QuizSetupForm(forms.ModelForm):
    questions = [
        'Favourite hobby',
        'Favorite animal',
        'Which place would you visit',
        'Favourite thing to do',
        'Favourite genre of music',
        'Favourite food',
        'One thing you would like to do everyday',
        'Favourite movie',
        'Favourite series',
        'How many languages do you speak'
    ]

    class Meta:
        model = QuizSetup
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',]

        q1_options = [
        'sleeping', 'reading', 'talking', 'playing'
        ]
        q2_options = [
        'dog', 'cat', 'mouse', 'rabbit'
        ]
        q3_options = [
        'africa', 'china', 'mexica', 'usa'
        ]
        q4_options = [
        'building', 'cooking', 'writing', 'coding'
        ]
        q5_options = [
        'gospel', 'rap', 'classical', 'rock'
        ]
        q6_options = [
        'cheese', 'sandwich', 'hotdog', 'rolls'
        ]
        q7_options = [
        'sleep', 'talk', 'move', 'exercise'
        ]
        q8_options = [
        'batman', 'blackwidow', 'flash', 'superman'
        ]
        q9_options = [
        'ben10', 'tom and jerry', 'transformers', 'cars'
        ]
        q10_options = [
        '1', '2', '3', '4'
        ]

        widgets = {
            'q1': forms.TextInput(attrs={'placeholder': f'eg: {q1_options[0]}'}),
            'q2': forms.TextInput(attrs={'placeholder': f'eg: {q2_options[0]}'}),
            'q3': forms.TextInput(attrs={'placeholder': f'eg: {q3_options[0]}'}),
            'q4': forms.TextInput(attrs={'placeholder': f'eg: {q4_options[0]}'}),
            'q5': forms.TextInput(attrs={'placeholder': f'eg: {q5_options[0]}'}),
            'q6': forms.TextInput(attrs={'placeholder': f'eg: {q6_options[0]}'}),
            'q7': forms.TextInput(attrs={'placeholder': f'eg: {q7_options[0]}'}),
            'q8': forms.TextInput(attrs={'placeholder': f'eg: {q8_options[0]}'}),
            'q9': forms.TextInput(attrs={'placeholder': f'eg: {q9_options[0]}'}),
            'q10': forms.TextInput(attrs={'placeholder': f'eg: {q10_options[0]}'}),
        }
class WorkdleSetupForm(forms.ModelForm):
    q_list = [
        'where do you want to live',
        'What is your biggest fear',
        'What is one thing you would change about yourself',
        'favourite music genre',
        'One thing you really really really want to buy'
    ]
    a_list = [
        'Africa',
        'spiders',
        'Impatience',
        'Country',
        'King bed'
    ]

    class Meta:
        model = WordleSetup
        fields = ['qq1','qq2', 'qq3', 'qq4', 'qq5', 'q1', 'q2', 'q3', 'q4', 'q5']

        q_list = [
            'eg: where do you want to live',
            'eg: What is your biggest fear',
            'eg: What is one thing you would change about yourself',
            'eg: favourite music genre',
            'eg: One thing you really really really want to buy'
        ]
        a_list = [
            'eg: Africa',
            'eg: spiders',
            'eg: Impatience',
            'eg: Country',
            'eg: King bed'
        ]
        widgets = {
            'qq1': forms.TextInput(attrs={'placeholder': f'{q_list[0]}'}),
            'qq2': forms.TextInput(attrs={'placeholder': f'{q_list[1]}'}),
            'qq3': forms.TextInput(attrs={'placeholder': f'{q_list[2]}'}),
            'qq4': forms.TextInput(attrs={'placeholder': f'{q_list[3]}'}),
            'qq5': forms.TextInput(attrs={'placeholder': f'{q_list[4]}'}),
            'q1': forms.TextInput(attrs={'placeholder': f'{a_list[0]}'}),
            'q2': forms.TextInput(attrs={'placeholder': f'{a_list[1]}'}),
            'q3': forms.TextInput(attrs={'placeholder': f'{a_list[2]}'}),
            'q4': forms.TextInput(attrs={'placeholder': f'{a_list[3]}'}),
            'q5': forms.TextInput(attrs={'placeholder': f'{a_list[4]}'}),
        }

class TtmaSetupForm(forms.ModelForm):
    question = "Easy things I enjoy talking about"

    class Meta:
        model = TtmaSetup
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']

        alist = [
            'eg: country music',
            'eg: batman',
            'eg: shooting games',
            'eg: cooking',
            'eg: differnt coffees',
            'eg: facebook animals'
        ]

        widgets = {
            'q1': forms.TextInput(attrs={'placeholder': f"{alist[0]}"}),
            'q2': forms.TextInput(attrs={'placeholder': f"{alist[1]}"}),
            'q3': forms.TextInput(attrs={'placeholder': f"{alist[2]}"}),
            'q4': forms.TextInput(attrs={'placeholder': f"{alist[3]}"}),
            'q5': forms.TextInput(attrs={'placeholder': f"{alist[4]}"}),
            'q6': forms.TextInput(attrs={'placeholder': f"{alist[5]}"}),
        }
