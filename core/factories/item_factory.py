import factory
from faker import Faker
from core.factories.company_factory import CompanyFactory

fake = Faker()

class ItemFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Item'
        django_get_or_create = ('title',)

    title = fake.name()
    company = factory.SubFactory(CompanyFactory)
