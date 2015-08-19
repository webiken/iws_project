from django.db import models

class Client(models.Model):
    """
        Client Model
    """
    name = models.CharField(max_length=100, null=False, blank=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class ProductArea(models.Model):
    """
        Product Area Model
    """
    product_area = models.CharField(max_length=100, null=False, blank=False)

    def __unicode__(self):
        return self.product_area

    def __str__(self):
        return self.__unicode__()


class FeatureRequest(models.Model):
    """
        This class represents the model definition for a database table for a Feature Request.
        
        The following fields are optional:
          - description
          - ticket_url

        All other fields are required.  The django framework will automatically create an ID field, that is also
        referensable as `pk`
    """
    product_area = models.ForeignKey(ProductArea)
    client = models.ForeignKey(Client)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    client_priority = models.IntegerField(null=False, blank=False)
    target_date = models.DateTimeField(null=False, blank=False)
    ticket_url = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()
