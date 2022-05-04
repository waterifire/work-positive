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
    q_options = [
        q1_options,
        q2_options,
        q3_options,
        q4_options,
        q5_options,
        q6_options,
        q7_options,
        q8_options,
        q9_options,
        q10_options,
    ]
    class Meta:
        model = QuizSetup
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',]

class WorkdleSetupForm(forms.ModelForm):
    questions = [
        'where do you want to live',
        'What is your biggest fear',
        'What is one thing you would change about yourself',
        'favourite music genre',
        'One thing you really really really want to buy'
    ]

    class Meta:
        model = WordleSetup
        fields = ['q1', 'q2', 'q3', 'q4', 'q5']


class TtmaSetupForm(forms.ModelForm):
    question = "Easy things I enjoy talking about"

    class Meta:
        model = TtmaSetup
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']
