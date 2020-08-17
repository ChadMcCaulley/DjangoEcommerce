import factory
from core.factories.locality import LocalityFactory


class AddressFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Address'
        django_get_or_create = (
            'street_address', 'additional_address', 'locality'
        )

    street_address = factory.Faker('street_address')
    additional_address = None
    locality = factory.SubFactory(LocalityFactory)
