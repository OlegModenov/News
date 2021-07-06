from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import News, Category
from .forms import NewsForm


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
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
    category = Category.objects.get(pk=category_id)
    context = {'news': news, 'category': category}
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    """ Возвращает конкретную новость """
    # news_item = News.objects.get(pk=news_id)

    # Чтобы отображалась нужная ошибка (404) в случае, если страницы нет
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_one.html', {'news_item': news_item})


def add_news(request):
    """ Возвращает форму добавления новости """
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewsForm()
    context = {'form': form}
    return render(request, 'news/add_news.html', context)
