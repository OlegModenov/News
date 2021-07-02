from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'creation_date', 'update_date', 'is_published')  # отобразить в админке
    list_display_links = ('id', 'title')  # Ссылки на новость в админке
    search_fields = ('title', 'content')  # Поля для поиска
    list_editable = ('is_published',)  # Можно сразу в списке убирать и ставить галочки
    list_filter = ('is_published', 'category')  # Добавляет в админку фильтр


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')  # Ссылки на новость в админке
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
