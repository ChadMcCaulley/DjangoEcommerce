import factory
from core.factories.company_factory import CompanyFactory


class ItemFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Item'
        django_get_or_create = ('title',)

    title = factory.Faker('name')
    company = factory.SubFactory(CompanyFactory)
