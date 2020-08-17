import factory
from core.factories.category import CategoryFactory
from core.factories.company import CompanyFactory

class ProductFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Product'
        django_get_or_create = ('title', 'company')

    title = factory.Faker('text', max_nb_chars=100)
    description = factory.Faker('text', max_nb_chars=500)
    price = factory.Faker('random_int')
    list_price = factory.Faker('random_int')
    quantity = factory.Faker('random_element', elements=(1, 5, 10, 20))
    inventory = factory.Faker('random_int')
    company = factory.SubFactory(CompanyFactory)
    category = factory.SubFactory(CategoryFactory)
