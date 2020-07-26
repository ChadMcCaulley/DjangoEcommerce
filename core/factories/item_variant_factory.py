import factory
from core.factories.item_factory import ItemFactory

class ItemVariantFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.ItemVariant'
        django_get_or_create = ('title', 'parent_item')

    parent_item = factory.SubFactory(ItemFactory)
    title = factory.Faker('text', max_nb_chars=100)
    price = factory.Faker('random_int')
    list_price = factory.Faker('random_int')
    quantity = factory.Faker('random_element', elements=(1, 5, 10, 20))
    inventory = factory.Faker('random_int')
    rating = factory.Faker('random_element', elements=(1,2,3,4,5))
    num_ratings = factory.Faker('random_int')
    