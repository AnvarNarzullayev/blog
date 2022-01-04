from django import template

from blog.models import Category
from taggit.models import Tag



register = template.Library()

@register.inclusion_tag('category.html')
def show_categories():
    categories = Category.objects.all().order_by('name')[:4]
    return {'categories':categories}

@register.inclusion_tag('tag.html')
def show_tags():
    tag = Tag.objects.all()
    return {'tag':tag}