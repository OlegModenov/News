from django import forms
from .models import Category, News


# # Реализация формы, не связанной с моедлью
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Содержание', required=False,
#                               widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
#     is_published = forms.BooleanField(label='Опубликовано', initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
#                                       empty_label='Выберите категорию',
#                                       widget=forms.Select(attrs={"class": "form-control"}))


# Реализация формы, связанной с моделью
class NewsForm(forms.ModelForm):
    # Настройка отображения категории
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'

    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control", "empty_label": 'sd'}),
        }
        labels = {
            'category': 'Выберите категорию'
        }
