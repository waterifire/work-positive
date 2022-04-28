from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.db.models import Q

from .models import Compliment
from .forms import ComplimentForm

from django.http import QueryDict

# Create your views here.


def compliment_home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    users = User.objects.filter(
        Q(username__icontains=q) |
        Q(email__icontains=q)
    )

    context = {'users': users, 'q_result': q}
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
            # return redirect('compliment_home')
            return redirect(request.path_info)
    else:
        context = {'user': user, 'form': form, 'compliments': compliments, 'q': q,}
        return render(request, 'compliment/compliment_user.html', context)
