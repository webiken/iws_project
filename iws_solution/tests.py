from django.test import TestCase
from django.utils import timezone

from iws_solution import models
from iws_solution import forms

class SaveFeatureTestCase(TestCase):

    def setUp(self):

        #create a client
        self.client = models.Client(name='Client A')
        self.client.save()

        #create a product area
        self.area = models.ProductArea(product_area='Billing')
        self.area.save()

        for i in range(1,6):
            title = 'title-%d' % i
            feature = models.FeatureRequest.objects.create(client=self.client, client_priority=i, product_area=self.area, title=title, target_date=timezone.now())

    def test_reorder_priority(self):
        data = dict(
            title='title',
            client_priority=3,
            product_area=1,
            client=self.client.pk,
            target_date='08/19/2015' 
        )

        form = forms.FeatureRequestForm(data=data)
        if form.is_valid():
            obj = form.save()

            #find featur with title-3, which should
            #now have a priority of 4
            existing_feaure = models.FeatureRequest.objects.get(client=self.client, title='title-3')
            self.assertEqual(obj.client_priority, 3)
            self.assertEqual(existing_feaure.client_priority, 4)