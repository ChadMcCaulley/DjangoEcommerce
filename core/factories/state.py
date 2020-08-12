import factory
from core.factories.country import CountryFactory


class StateFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.State'
        django_get_or_create = (
            'name', 'code', 'country'
        )

    name = factory.Faker('state_abbr')
    code = factory.Faker('state_abbr')
    country = factory.SubFactory(CountryFactory)
