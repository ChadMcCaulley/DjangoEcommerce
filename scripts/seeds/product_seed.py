import json
import os
import requests
from datetime import datetime
from random import randint, random

from core.factories import (
    CommentFactory,
    CompanyFactory,
    CategoryFactory,
    ProductFactory,
    ReviewFactory,
    UserFactory,
)
from core.models import Category, ProductImage
from scripts.seeds.seed_categories import seed_categories
from utils import get_image_from_url

owners = UserFactory.create_batch(10)
users = [u for u in owners]

def seed_images (images, file_name, product):
    for index, url in enumerate(images, start=1):
        image = get_image_from_url(url, f"{file_name}_{index}")
        ProductImage.objects.get_or_create(product=product, image=image)

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

def seed_products (products, company):
    for prod in products:
        prod['company'] = company
        prod['category'] = Category.objects.get(name=prod['category'])
        if not 'quantity' in prod:
            prod['quantity'] = 1
        images = prod['images']
        del prod['images']
        newProduct = ProductFactory(**prod)
        seed_images(images, prod['title'], newProduct)
        seed_reviews(newProduct)

def seed_companies (companies):
    for company in companies:
        compObj = CompanyFactory(
            name=company['name'],
            owner=owners[randint(0, len(owners) - 1)]
        )
        seed_products(company['products'], compObj)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
seed_dir = os.path.join(base_dir, "seeds/product_seed.json")
with open(seed_dir) as products_file:
    obj = json.load(products_file)
    seed_categories(obj['categories'])
    seed_companies(obj['companies'])
    
