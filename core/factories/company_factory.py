import factory
from core.factories.user_factory import UserFactory
from core.factories.country_factory import CountryFactory
from core.factories.state_factory import StateFactory
from core.factories.city_factory import CityFactory


class CompanyFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Company'
        django_get_or_create = ('name',)

    name = factory.Faker('company')
    website = 'https://github.com/ChadMcCaulley'
    owner = factory.SubFactory(UserFactory)
    address = factory.Faker('street_address')
    country = factory.SubFactory(CountryFactory)
    state = factory.SubFactory(StateFactory)
    city = factory.SubFactory(CityFactory)
    zip_code = factory.Faker('postcode')