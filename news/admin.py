from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


# CKEditor
class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm  # использование CKEditor
    # отображение в админке всех новостей
    list_display = ('id', 'title', 'category', 'creation_date', 'update_date', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')  # Ссылки на новость в админке
    search_fields = ('title', 'content')  # Поля для поиска
    list_editable = ('is_published',)  # Можно сразу в списке убирать и ставить галочки
    list_filter = ('is_published', 'category')  # Добавляет в админку фильтр

    # Отображение в админке отдельной новости
    fields = ('title', 'category', 'content', 'photo', 'is_published', 'get_photo', 'views', 'creation_date',
              'update_date')
    readonly_fields = ('get_photo', 'views', 'creation_date', 'update_date')

    # Отображение фото

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return "Фото не установлено"

    get_photo.short_description = "Фото"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')  # Ссылки на новость в админке
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
