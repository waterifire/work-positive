from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .models import Compliment
from .forms import ComplimentForm

# Create your views here.


def compliment_home(request):
    users = User.objects.filter()

    context = {'users': users,}
    return render(request, 'compliment/compliment_home.html', context)



def compliment_user(request, pk):
    user = User.objects.get(id=pk)
    compliments = Compliment.objects.all()
    form = ComplimentForm()

    if request.method == "POST":
        form = ComplimentForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.receiver = user.username
            comp.giver = request.user
            comp.save()
            return redirect('compliment_home')
    else:
        context = {'user': user, 'form': form, 'compliments': compliments,}
        return render(request, 'compliment/compliment_user.html', context)
