import factory
from factory.faker import faker

from .models import Post
from django.contrib.auth.models import User

FAKE = faker.Faker()

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence', nb_words=12)
    sub_title = factory.Faker('sentence', nb_words=12)
    slug = factory.Faker('slug')
    author = User.objects.get_or_create(username='blog_admin')[0]

    @factory.lazy_attribute
    def content(self):
        x = ''
        for _ in range(0, 5):
            x += '\n' + FAKE.paragraph(nb_sentences=30) + '\n'
        return x

    status = 'published'