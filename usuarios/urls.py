from django.conf.urls import url
from django.urls import include, path
from usuarios.views import CerrarSesionView,LoginView
app_name = 'usuarios'


urlpatterns = [

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^cerrar-sesion/$', CerrarSesionView.as_view(), name='cerrar-sesion'),
    #url(r'^rest-auth/', include('rest_auth.urls')),
]