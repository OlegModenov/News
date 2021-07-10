from django import template
from django.db.models import Count
from django.db.models import F

from news.models import Category

register = template.Library()


# Реализация вывода sidebar через simple_tag
@register.simple_tag()
def get_categories():
    # Возвращаем только непустые категории (те категории, которые опубликованы и количество записей которых больше 0)
    return Category.objects.annotate(amount=Count('news', filter=F('news__is_published'))).filter(amount__gt=0)


# Реализация вывода sidebar через inclusion_tag
# @register.inclusion_tag('news/list_categories.html')
# def show_categories():
#     categories = Category.objects.all()
#     context = {'categories': categories}
#     return context
