from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()


# Реализация вывода sidebar через simple_tag
@register.simple_tag()
def get_categories():
    # Возвращаем только непустые категории (те категории, количество записей которых больше 0)
    return Category.objects.annotate(amount=Count('news')).filter(amount__gt=0)


# Реализация вывода sidebar через inclusion_tag
# @register.inclusion_tag('news/list_categories.html')
# def show_categories():
#     categories = Category.objects.all()
#     context = {'categories': categories}
#     return context
