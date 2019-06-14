from django.conf.urls import url
from .views import *

app_name = 'croquis_listado'
urlpatterns = [
    url(r'^monitoreo/$', CroquisListadoView.as_view(), name='monitoreo'),
]
