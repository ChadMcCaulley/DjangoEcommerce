import random
from core.factories import (
    ProductFactory, ReviewFactory, CommentFactory,
    UserFactory, CompanyFactory
)
from scripts.seeds.seed_categories import seed_categories

seed_categories(
    ["Electronics", "Clothing", "Footware", "Luggage", "Bicycle"]
)


owners = UserFactory.create_batch(10)
users = [u for u in owners]

def seed_comments (review):
    for i in range(randint(0, 5)):
        comm_user = None
        if random() > 0.1:
            comm_user = users[randint(0, len(users) - 1)]
        else:
            comm_user = UserFactory()
            users.append(comm_user)
        CommentFactory(review=review, user=comm_user)

def seed_reviews (product):
    poss_users = users.copy()
    for i in range(randint(0, 30)):
        review_user = None
        if random() > 0.1 and len(poss_users) > 0:
            index = randint(0, len(poss_users) - 1)
            review_user = poss_users[index]
            del poss_users[index]
        else:
            review_user = UserFactory()
            users.append(review_user)
        review = ReviewFactory(product=product, user=review_user)
        seed_comments(review)

def seed_products (companies):
    for company in companies:
        products = ProductFactory.create_batch(
            random.randint(0, 5), company=company
        )
        seed_reviews(products)

def seed_companies (owners):
    for owner in owners:
        companies = CompanyFactory.create_batch(
            random.randint(0, 2), owner=owner
        )
        seed_products(companies)


seed_companies(owners)