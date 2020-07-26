import factory


class CityFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.City'
        django_get_or_create = ('name',)

    name = factory.Faker('city')