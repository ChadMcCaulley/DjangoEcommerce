import factory


class StateFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.State'
        django_get_or_create = ('name','code')

    name = factory.Faker('state')
    code = factory.Faker('state_abbr')