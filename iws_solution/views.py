import json
from datetime import datetime

from django import http
from django.shortcuts import render
from django.db import transaction
from django.core.urlresolvers import reverse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from iws_solution.forms import FeatureRequestForm
from iws_solution.models import FeatureRequest, Client, ProductArea

def is_valid_url(url):
    """
        This function validates a given URL
    """
    val = URLValidator()
    try:
        val(url)
        return True
    except ValidationError, e:
        return False

# if an exception occurs transactions are rolledback
@transaction.atomic
def home(request, template='index.html'):
    """
        This is the home route's view.  
        It is used to load the new FeatureRequest form, and save it.
        It's decorated with transaction.atormic to rollback transactions
        upon errors.
    """
    context = dict()
    
    if request.method == 'GET':
        form = FeatureRequestForm()
    else:
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect(reverse('list', args=(form.cleaned_data.get('client').pk,)))

    context['form'] = form
    return render(request, template, context)

def list_features(request, client_id=None, template='list.html'):
    """
        The is the view to list the features per client.
        The drop down for the client will update the table.
    """
    if client_id:
        client_id = int(client_id)
        features = FeatureRequest.objects.filter(client=client_id).order_by('client_priority')
    else:
        features = []

    return render(request, template, dict(features=features, client_id=client_id, product_areas=ProductArea.objects.all(), clients=Client.objects.all()))

def edit_feature(request):
    """
       This Ajax view updates the feature from the feature list table.
       Using the Boostrap plugin, an ajax post is made.
       We validate the ticket_url and target_date to ensure
       data consistency. 
    """
    if not request.is_ajax():
        raise http.Http404

    feature = FeatureRequest.objects.get(pk=request.POST.get('pk'))

    if request.POST.get('name') in ['target_date', 'ticket_url']:
        if request.POST.get('name') == 'target_date':
            #validate the date
            try:
                target_date = datetime.strptime(request.POST.get('value'), '%b %d, %Y')
                feature.target_date = target_date
                feature.save()
            except Exception as e:
                raise RuntimeError("Invalid date %s" % request.POST.get('value'))

        else:
            #validate the ticket_url
            if is_valid_url(request.POST.get('value')):
                feature.ticket_url = request.POST.get('value')
                feature.save()
            else:
                raise RuntimeError("Invalid URL %s" % request.POST.get('value'))

    else:
        setattr(feature, request.POST.get('name'), request.POST.get('value'))
        #make sure to save the feature
        feature.save()

    return http.HttpResponse(json.dumps({'value': request.POST.get('value')}), content_type="application/json")

