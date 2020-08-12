import factory
from core.factories.state import StateFactory


class LocalityFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Locality'
        django_get_or_create = (
            'name', 'postal_code', 'state'
        )

    name = factory.Faker('city')
    postal_code = factory.Faker('postcode')
    state = factory.SubFactory(StateFactory)
