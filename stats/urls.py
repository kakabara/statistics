from django.conf.urls import url
from . import views


urlpatterns = [
    url('load_data/', view=views.loader, name='data_loader'),
    url('get_stats/', view=views.stats, name='stats'),
    # url('/', view=views.index, name='index'),
]