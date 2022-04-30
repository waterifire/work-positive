from django.shortcuts import render

from test_setup.models import QuizSetup
from test_setup.forms import QuizSetupForm
# Create your views here.

def dykt_home(request):
    people = QuizSetup.objects.all()

    context = {'people': people}
    response = render(request, 'dykt/dykt_home.html', context)
    return response


def dykt_arena(request, pk):
    person = QuizSetup.objects.get(id=pk)
    form = QuizSetupForm(instance=person)
    context = {'person': person, 'form': form}
    response = render(request, 'dykt/dykt_arena.html', context)
    return response
