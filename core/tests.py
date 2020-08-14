from django.test import TestCase
from core.models import Product
from core.factories import ProductFactory, ReviewFactory

class ProductTests (TestCase):

    def test_product_review_signals (self):
        """Product rating changes when reviews are added and removed"""
        product = ProductFactory()
        self.assertEqual(product.rating, None)
        self.assertEqual(product.num_reviews, 0)
        review = ReviewFactory(rating=1, product=product)
        review2 = ReviewFactory(rating=5, product=product)
        self.assertEquals(product.rating, 3)
        self.assertEquals(product.num_reviews, 2)
        review.delete()
        review2.delete()
        self.assertEquals(product.rating, None)
        self.assertEquals(product.num_reviews, 0)