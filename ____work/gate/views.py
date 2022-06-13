from django.shortcuts import render


from .models import Bio
from .forms import BioForm
# Create your views here.


def enter_gate(request):
    bios = Bio.objects.all()
    bioF = BioForm()

    context = {'bioF': bioF, 'bios': bios,}
    response = render(request, 'gate/enter_gate.html', context)
    return response

