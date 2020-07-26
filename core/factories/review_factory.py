import factory
from core.factories.user_factory import UserFactory
from core.factories.item_variant_factory import ItemVariantFactory

class ReviewFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Review'

    title = factory.Faker('text', max_nb_chars=100)
    message = factory.Faker('text', max_nb_chars=280)
    rating = factory.Faker('random_element', elements=(1, 2, 3, 4, 5))
    item = factory.SubFactory(ItemVariantFactory)
    user = factory.SubFactory(UserFactory)
