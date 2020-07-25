import factory
from faker import Faker

fake = Faker()

class CountryFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Country'
        django_get_or_create = ('name','code')

    name = fake.country()
    code = fake.country_code()