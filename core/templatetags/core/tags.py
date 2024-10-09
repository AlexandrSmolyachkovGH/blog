from django import template
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag('core/components/tags.html')
def add_tag():
    tags = Tag.objects.all()
    return {'tags': tags}
