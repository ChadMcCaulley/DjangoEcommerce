import factory
from core.factories.user import UserFactory
from core.factories.review import ReviewFactory


class CommentFactory (factory.DjangoModelFactory):
    class Meta:
        model = 'core.Comment'

    title = factory.Faker('text', max_nb_chars=100)
    message = factory.Faker('text', max_nb_chars=280)
    review = factory.SubFactory(ReviewFactory)
    parent_comment = None
    user = factory.SubFactory(UserFactory)