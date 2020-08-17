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

def seed_comments (reviews):
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

def seed_reviews (products):
    for product in products:
        reviewUser = None
        if random.random() > 0.1:
            reviewUser = users[random.randint(0, len(users) - 1)]
        else:
            reviewUser = UserFactory()
            users.append(reviewUser)
        reviews = ReviewFactory.create_batch(
            random.randint(0, 10), product=product, user=reviewUser
        )
        seed_comments(reviews)

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