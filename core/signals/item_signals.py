from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.models import Item, Review, ItemVariant

@receiver(post_save, sender=Review)
@receiver(post_delete, sender=Review)
def update_item_variant_rating(sender, instance, **kwargs):
    reviews = instance.item.review_set.all()
    num_ratings = reviews.count()
    instance.item.num_ratings = num_ratings
    total_ratings = 0
    rating = None
    for review in reviews:
        total_ratings += review.rating
    if num_ratings > 0:
        rating = total_ratings / num_ratings
    instance.item.rating = rating
    instance.item.save()
