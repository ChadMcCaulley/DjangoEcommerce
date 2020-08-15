from django.core.exceptions import ValidationError
from django.test import TestCase
from core.models import Product
from core.factories import ProductFactory, ReviewFactory, CommentFactory

class ProductTests (TestCase):
    """Test cases for the product model"""

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

class CommentTests (TestCase):
    """Test cases for the comment model"""

    def test_must_have_parent (self):
        """Comments must have either a review or comment as a parent"""
        with self.assertRaises(ValidationError) as context:
            CommentFactory(review=None, parent_comment=None)

        self.assertTrue(
            'Comments must have a parent comment or review' \
            in context.exception
        )