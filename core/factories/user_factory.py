import factory
from django.conf import settings


class UserFactory (factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('email','username', 'first_name', 'last_name')

    username = factory.Faker('text', max_nb_chars=50)
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    email = factory.Faker('ascii_company_email')
    password = factory.PostGenerationMethodCall(
        'set_password', 'password')
    
    is_superuser = False
    is_staff = False
    is_active = True