from django.urls import path, include

from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('test/', test),
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('', cache_page(60)(HomeNews.as_view()), name='home'),  # Вариант с кэшированием
    # path('category/<int:category_id>/', get_category, name='news_of_category'),
    path('category/<int:category_id>/', NewsOfCategory.as_view(), name='index'),
    # path('news/<int:news_id>/', view_news, name='news_one'),
    path('news/<int:pk>/', NewsOne.as_view(), name='news_one'),  # Можно через <int:pk> и <int:id>, лучше pk
    # path('news/add_news/', add_news, name='add_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path('sign_up/', sign_up, name='sign_up'),
    path('log_in/', user_login, name='log_in'),
    path('log_out/', user_logout, name='log_out'),
    path('mail', mail, name='mail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]