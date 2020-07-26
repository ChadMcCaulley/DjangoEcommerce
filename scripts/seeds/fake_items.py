import random
from core.factories import (
    ItemVariantFactory, ItemFactory, ReviewFactory, CommentFactory,
    UserFactory, CompanyFactory
)


owners = UserFactory.create_batch(10)
users = [u for u in owners]
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
            for variant in variants:
                reviewUser = None
                if random.random() > 0.1:
                    reviewUser = users[random.randint(0, len(users) - 1)]
                else:
                    reviewUser = UserFactory()
                    users.append(reviewUser)
                reviews = ReviewFactory.create_batch(
                    random.randint(0, 10), item=variant, user=reviewUser
                )
                for review in reviews:
                    comUser = None
                    if random.random() > 0.1:
                        comUser = users[
                            random.randint(0, len(users) - 1)]
                    else:
                        comUser = UserFactory()
                    users.append(comUser)
                    comments = CommentFactory.create_batch(
                        random.randint(0, 3), review=review, user=comUser
                    )
                    print(comments)