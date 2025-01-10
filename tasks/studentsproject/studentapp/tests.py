from django.test import TestCase

from model_bakery import baker

class PurchaseHistoryTestModel(TestCase):

    def setUp(self):
        self.history = baker.make('shop.PurchaseHistory')
        print(self.history.customer)