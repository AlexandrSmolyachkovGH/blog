from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
class Post(models.Model):

    options = [
        ('published', 'published'),
        ('draft', 'draft')
    ]

    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default='draft')

    tags = TaggableManager()

    class Meta:
        ordering = ('-create_time',) #Newest posts at top

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_single', args=[self.slug])
