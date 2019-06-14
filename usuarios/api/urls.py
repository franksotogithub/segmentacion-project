from django.conf.urls import url
from django.urls import include, path
#from usuarios.views import CerrarSesionView,LoginView
from usuarios.api.views import AuthViewSet

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
router = DefaultRouter()
app_name = 'usuarios_api'

router.register(r'auth',AuthViewSet,base_name='auth')

urlpatterns = [
        url(r'^rest-auth/', include('rest_auth.urls')),
        url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
        url(r'^api-token-auth/', obtain_jwt_token),
        #url(r'^auth/', AuthViewSet.as_view() , name='auth'),
        #url(r'^login/$', LoginView.as_view(), name='login'),
        #url(r'^cerrar-sesion/$', CerrarSesionView.as_view(), name='cerrar-sesion'),
        #url(r'^rest-auth/', include('rest_auth.urls')),
]

urlpatterns += router.urls