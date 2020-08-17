import factory
from core.factories.address import AddressFactory
from core.factories.user import UserFactory


class CompanyFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Company'
        django_get_or_create = ('name',)

    name = factory.Faker('company')
    website = 'https://github.com/ChadMcCaulley'
    owner = factory.SubFactory(UserFactory)
    address = factory.SubFactory(AddressFactory)
