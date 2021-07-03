from django import template

from news.models import Category

register = template.Library()


# Реализация вывода sidebar через simple_tag
@register.simple_tag()
def get_categories():
    return Category.objects.all()


# Реализация вывода sidebar через inclusion_tag
# @register.inclusion_tag('news/list_categories.html')
# def show_categories():
#     categories = Category.objects.all()
#     context = {'categories': categories}
#     return context