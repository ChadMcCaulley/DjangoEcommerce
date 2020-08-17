from core.factories import CategoryFactory

def seed_categories(category_names):
    for name in category_names:
        CategoryFactory(name=name)