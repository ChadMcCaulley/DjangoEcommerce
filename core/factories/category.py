import factory


class CategoryFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Category'
        django_get_or_create = ('name',)

    name = factory.Faker('name')
