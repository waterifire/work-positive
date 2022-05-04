from django.shortcuts import render

from test_setup.models import TtmaSetup
from test_setup.forms import TtmaSetupForm

# Create your views here.

def ttma_home(request):
    people = TtmaSetup.objects.all()

    context = {'people': people,}
    response = render(request, 'ttma/ttma_home.html', context)
    return response
