from django.test import TestCase
from core.models import Product
from core.factories import ProductFactory, ReviewFactory

class ProductTests (TestCase):
    def setUp(self):
        self.product = ProductFactory()

    def test_product_review_signal(self):
        """Product rating changed when review added"""
        self.assertEqual(self.product.rating, None)
        self.assertEqual(self.product.num_reviews, 0)
        ReviewFactory(rating=2, product=self.product)
        ReviewFactory(rating=5, product=self.product)
        ReviewFactory(rating=2, product=self.product)
        ReviewFactory(rating=5, product=self.product)
        self.assertEquals(self.product.rating, 3.5)
        self.assertEquals(self.product.num_reviews, 4)