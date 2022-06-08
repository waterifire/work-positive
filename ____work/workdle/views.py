from django.shortcuts import render
import random

from test_setup.models import WordleSetup
from test_setup.forms import WorkdleSetupForm
# Create your views here.

def workdle_home(request):
    people = WordleSetup.objects.all()
    context = {'people': people,}
    response = render(request, 'workdle/workdle_home.html', context)
    return response

def workdle_arena(request, pk):
    color_test = 'deepskyblue'
    person = WordleSetup.objects.get(id=pk)
    form = WorkdleSetupForm(instance=person)

    number_options = [0, 1, 2, 3, 4]
    number_choice = random.choice(number_options)
    question_options = [person.qq1, person.qq2, person.qq3, person.qq4, person.qq5]
    word_options = [person.q1, person.q2, person.q3, person.q4, person.q5]

    word_specific = word_options[number_choice].lower()
    word_length = int(len(word_specific))
    question_specific = question_options[number_choice]

    context = {'question_specific': question_specific, 'word_length': word_length, 'word_specific': word_specific, 'person': person, 'form': form, 'color_test': color_test}
    response = render(request, 'workdle/workdle_arena.html', context)
    return response
