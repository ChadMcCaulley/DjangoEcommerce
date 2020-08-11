from django.db import models
from core.datatypes import NullableDecimal
from core.mixins import TimeStampMixin


class ProductLine(TimeStampMixin):
    """
    Parent entity to connect multiple products in a company's
    catalog of products.
    Ex. Shirts with multiple colors
    Ex. Same masks sold in different quantities and prices
    """
    class Meta:
        verbose_name_plural='Product Lines'
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='products'
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    rating = NullableDecimal(
        max_digits=2, decimal_places=1, editable=False
    )
    num_ratings = models.PositiveIntegerField(default=0, editable=False)

    @property
    def rating_breakdown (self):
        ratings = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        result = {}
        for review in self.review_set.all():
            ratings[review.rating] += 1
        for rating in ratings.items():
            result[rating[0]] = round(rating[1] / self.num_ratings, 4)
        return result

    def __str__(self):
        return f'{self.company.name}_{self.title}'