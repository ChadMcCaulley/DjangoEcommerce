import factory
from faker import Faker

fake = Faker()

class CityFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.City'
        django_get_or_create = ('name',)

    name = fake.city()