import factory


class CountryFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Country'
        django_get_or_create = (
            'name', 'code'
        )

    name = factory.Faker('country')
    code = factory.Faker('country_code')
