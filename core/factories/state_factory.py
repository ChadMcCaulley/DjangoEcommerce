import factory
from faker import Faker

fake = Faker()

class StateFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.State'
        django_get_or_create = ('name','code')

    name = fake.state()
    code = fake.state_abbr()