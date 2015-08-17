from django import http
from django.shortcuts import render

from iws_solution.forms import FeatureRequestForm

def home(request, template='index.html'):
    context = dict()
    
    if request.method == 'GET':
        form = FeatureRequestForm()

    context['form'] = form
    return render(request, template, context)
