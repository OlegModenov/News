from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    # так как модель категории создавалась позже, нужно поставить null=True, чтобы удалось выполнить миграции
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-creation_date', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Функция reverse - аналог тега url в шаблоне. Данные функции строят ссылку в py и html файлах соответственно
        # Передаем в reverse название маршрута и параметр для построения данного маршрута
            return reverse('news_one', kwargs={'news_id': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Функция reverse - аналог тега url в шаблоне. Данные функции строят ссылку в py и html файлах соответственно
        # Передаем в reverse название маршрута и параметр для построения данного маршрута
        return reverse('category', kwargs={'category_id': self.pk})


