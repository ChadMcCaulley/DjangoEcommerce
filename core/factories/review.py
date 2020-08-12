import factory
from core.factories.user import UserFactory
from core.factories.product_line import ProductLineFactory

class ReviewFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Review'

    title = factory.Faker('text', max_nb_chars=100)
    message = factory.Faker('text', max_nb_chars=280)
    rating = factory.Faker('random_element', elements=(1, 2, 3, 4, 5))
    product = factory.SubFactory(ProductLineFactory)
    user = factory.SubFactory(UserFactory)
