# from django.conf import settings

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('test/', test),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='news_one'),
    path('news/add_news/', add_news, name='add_news'),
]

# Формирование маршрута, по которому Django отдает медиафайлы (в отладочном режиме).
# В обычном режиме все будет работать по умолчанию
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)