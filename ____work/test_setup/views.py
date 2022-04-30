from django.shortcuts import render, redirect

from .models import QuizSetup
from .forms import QuizSetupForm
# Create your views here.

def ts_home(request):

    context = {}
    response = render(request, 'ts/ts_home.html', context)
    return response

def ts_quiz(request):

    form = QuizSetupForm()


    if request.method == "POST":
        form = QuizSetupForm(request.POST)
        if form.is_valid():
            more_details = form.save(commit=False)
            more_details.quiz_about = request.user
            more_details.save()
            return redirect('ts_home')

    context = {'form': form,}

    response = render(request, 'ts/ts_quiz.html', context)
    return response
