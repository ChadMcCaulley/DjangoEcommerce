import factory
from core.factories.company import CompanyFactory
from core.factories.category import CategoryFactory


class ProductLineFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.ProductLine'
        django_get_or_create = ('title',)

    title = factory.Faker('name')
    description = factory.Faker('text', max_nb_chars=500)
    company = factory.SubFactory(CompanyFactory)
    category = factory.SubFactory(CategoryFactory)
    rating = None
    num_ratings = 0
