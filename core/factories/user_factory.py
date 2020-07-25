import factory
from django.conf import settings
from faker import Faker

fake = Faker()

class UserFactory (factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('email',)

    username = fake.simple_profile()['username']
    email = fake.ascii_free_email()
    password = factory.PostGenerationMethodCall('set_password', 'password')
    
    is_superuser = False
    is_staff = False
    is_active = True