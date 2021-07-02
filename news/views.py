from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories
    }
    return render(request, 'news/index.html', context)


def test(request):
    return HttpResponse('<h1> Тестовая страница </h1>')


def get_category(request, category_id):
    """
    Возвращает новости в данной категории
    Второй параметр (category_id) - получает из urls.py (category/<int:category_id>/)
    """
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {'news': news, 'categories': categories, 'category': category}
    return render(request, 'news/category.html', context)

