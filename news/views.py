from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm


def test(request):
    return HttpResponse('<h1> Тестовая страница </h1>')

# # Реализация представления через функцию
# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context)


# Реализация представления через класс
class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'  # шаблон, по умолчанию news/news_list.html для ListView
    context_object_name = 'news'  # Объект в шаблоне, по умолчанию object_list для ListView

    def get_context_data(self, *, object_list=None, **kwargs):
        """ Возвращает контекст для шаблона """
        context = super().get_context_data(**kwargs)  # Сохраняем старые значения
        context['title'] = 'Главная страница'  # Добавляем новые значения
        return context

    # Возваращает queryset, по умолчанию News.objects.all()
    def get_queryset(self):
        return News.objects.filter(is_published=True)


# def get_category(request, category_id):
#     """
#     Возвращает новости в данной категории
#     Второй параметр (category_id) - получает из urls.py (category/<int:category_id>/)
#     """
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {'news': news, 'category': category}
#     return render(request, 'news/news_of_category.html', context)


class NewsOfCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False  # Не выводить пустые списки с категориями

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        # будет формироваться запрос: выбрать новости, где is_published == true и category_id = номер категории,
        # который получен из файла urls.py в путях
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id'])


# def view_news(request, news_id):
#     """ Возвращает конкретную новость """
#     # news_item = News.objects.get(pk=news_id)
#
#     # Чтобы отображалась нужная ошибка (404) в случае, если страницы нет
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/news_one.html', {'news_item': news_item})


class NewsOne(DetailView):
    model = News
    template_name = 'news/news_one.html'
    context_object_name = 'news_item'


# def add_news(request):
#     """ Возвращает форму добавления новости в случае get-запроса
#         Производит валидацию, заносит данные в базу и переходит на страницу с новость в случае post-запроса """
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)  # Для формы, не связнанной с моделью
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     context = {'form': form}
#     return render(request, 'news/add_news.html', context)


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # Также в модели должен быть определен метод get_absolute_url, тогда будет автоматическое перенаправление на
    # нужную страницу. Если этот метод не определен, то можно использовать success_url:
    # success_url = reverse_lazy('home')
