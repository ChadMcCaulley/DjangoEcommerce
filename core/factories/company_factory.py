import factory
from faker import Faker
from core.factories.user_factory import UserFactory
from core.factories.country_factory import CountryFactory
from core.factories.state_factory import StateFactory
from core.factories.city_factory import CityFactory

fake = Faker()

class CompanyFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Company'
        django_get_or_create = ('name',)

    name = fake.company()[:100]
    website = 'https://github.com/ChadMcCaulley'
    owner = factory.SubFactory(UserFactory)
    address = fake.street_address()
    country = factory.SubFactory(CountryFactory)
    state = factory.SubFactory(StateFactory)
    city = factory.SubFactory(CityFactory)
    zip_code = fake.postcode()