# from django.conf import settings

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('test/', test),
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='news_of_category'),
    path('category/<int:category_id>/', NewsOfCategory.as_view(), name='index'),
    # path('news/<int:news_id>/', view_news, name='news_one'),
    path('news/<int:pk>/', NewsOne.as_view(), name='news_one'),  # Можно через <int:pk> и <int:id>, лучше pk
    # path('news/add_news/', add_news, name='add_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
]

# Формирование маршрута, по которому Django отдает медиафайлы (в отладочном режиме).
# В обычном режиме все будет работать по умолчанию
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)