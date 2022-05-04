from django.shortcuts import render

# Create your views here.

def salvation_home(request):
    context = {}
    response = render(request, 'salvation/salvation_home.html', context)
    return response
