from django import forms

from iws_solution.models import FeatureRequest

class FeatureRequestForm(forms.ModelForm):
    
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'client', 'client_priority', 'target_date', 'ticket_url', 'product_area']