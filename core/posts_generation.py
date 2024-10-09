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

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, or nothing to add, do nothing.
            return
        if extracted:
            self.tags.add(extracted)
        else:
            self.tags.add("fun", "mem", "python", "code", "blog", "technology", "design", "learning", "interesting", "entertainment", 'sport', 'wow-content', 'lol')
