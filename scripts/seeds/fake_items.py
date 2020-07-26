import random
from core.factories import (
    ItemVariantFactory, ItemFactory, ReviewFactory, CommentFactory,
    UserFactory, CompanyFactory
)

owners = UserFactory.create_batch(10)
for owner in owners:
    companies = CompanyFactory.create_batch(
        random.randint(0, 2), owner=owner
    )
    for company in companies:
        items = ItemFactory.create_batch(
            random.randint(0, 5), company=company
        )            
        for item in items:
            variants = ItemVariantFactory.create_batch(
                random.randint(0, 5), parent_item=item
            )
            print(variants)
            for variant in variants:
                reviews = ReviewFactory.create_batch(
                    random.randint(0, 10), item=variant
                )
                for review in reviews:
                    comments =CommentFactory.create_batch(
                        random.randint(0, 3), review=review
                    )