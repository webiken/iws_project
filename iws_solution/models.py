from django.db import models

class FeatureRequest(models.Model):
    """
        This class represents the model definition for a database table for a Feature Request.
        
        The following fields are optional:
          - description
          - ticket_url

        All other fields are required.  The django framework will automatically create an ID field, that is also
        referensable as `pk`
    """
    CLIENT_CHOICES = (
        ('A', 'Client A'),
        ('B', 'Client B'),
        ('C', 'Client C'),
    )
    PRODUCT_CHOICES = (
        ('P', 'Policies'),
        ('B', 'Billing'),
        ('C', 'Claims'),
        ('R', 'Reports'),
    )

    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    client = models.CharField(max_length=1, choices=CLIENT_CHOICES)
    client_priority = models.IntegerField(null=False, blank=False)
    target_date = models.DateTimeField(null=False, blank=False)
    ticket_url = models.CharField(max_length=200, null=True, blank=True)
    product_area = models.CharField(max_length=1, choices=PRODUCT_CHOICES)