from django.conf.urls import url
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('get_info/', view=views.get_info, name='get_info'),
    path('load_data/', view=views.loader, name='data_loader'),
    path('get_stats/', view=views.stats, name='stats'),
    path('', view=views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)