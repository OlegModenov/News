import re
from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Category, News

# # Реализация формы, не связанной с моделью
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Содержание', required=False,
#                               widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
#     is_published = forms.BooleanField(label='Опубликовано', initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
#                                       empty_label='Выберите категорию',
#                                       widget=forms.Select(attrs={"class": "form-control"}))


# Реализация аналогичной формы, связанной с моделью
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

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # Переопределяем для изменения внешнего вида (widget)
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}),
                               help_text='Обязательное поле. Не более 150 символов')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
