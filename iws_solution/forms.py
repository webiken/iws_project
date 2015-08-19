from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError

from iws_solution import models as iws_models

def validate_positive(value):
    """
        Validate that the client prority is
        greater or equal to 1
    """
    if value < 1:
        raise ValidationError('%s must be greater than zero' % value)

def validate_future(value):
    """
        Ensure the target_date is in the future
    """
    if value < timezone.now():
        raise ValidationError('%s must be in the future' % value.strftime('%m-%d-%Y') )

class FeatureRequestForm(forms.ModelForm):
    """
        This model form is used to create a new feature request.
        Since feature requests are client based, we first lookup
        any feature requests for that client with the given priority.
        If none found, continue, else increase existing priorities by 1
    """

    client_priority = forms.IntegerField(validators=[validate_positive])
    target_date = forms.DateTimeField(validators=[validate_future])
    ticket_url = forms.URLField(required=False)

    class Meta:
        model = iws_models.FeatureRequest
        fields = ['title', 'description', 'client', 'client_priority', 'target_date', 'ticket_url', 'product_area']

    def save(self, *args, **kwargs):
        data = self.cleaned_data
        client = data['client']
        try:
            # first we want to verify that this feature priority doesn't exist for the client
            existing_feature = iws_models.FeatureRequest.objects.get(client=client, client_priority=data['client_priority'])

            # if a client already has this feature priority, we add 1 to all features with a higher priority than this feature
            existing_features = iws_models.FeatureRequest.objects.filter(client=client, client_priority__gte=data['client_priority'])

            #don't save unless this current feature saves
            for feature in existing_features:
                feature.client_priority += 1

        except iws_models.FeatureRequest.DoesNotExist as e:
            existing_features = []


        obj = super(FeatureRequestForm, self).save(*args, **kwargs)

        # now save the existing features with their new priority
        for feature in existing_features:
            feature.save()

        return obj
        
