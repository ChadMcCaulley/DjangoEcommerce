import factory
from django.conf import settings


class UserFactory (factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('email','username')

    username = factory.Faker('name')
    email = factory.Faker('ascii_free_email')
    password = factory.PostGenerationMethodCall(
        'set_password', 'password')
    
    is_superuser = False
    is_staff = False
    is_active = True