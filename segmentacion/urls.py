"""segmentacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^croquis_listado_api/',include('croquis_listado.api.urls',namespace='croquis_listado_api')),
    url(r'^croquis_listado/',include('croquis_listado.urls',namespace='croquis_listado')),
    url(r'^usuarios/',include('usuarios.urls',namespace='usuarios')),
    url(r'^usuarios/api/',include('usuarios.api.urls',namespace='usuarios_api')),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    #url(r'^rest-auth/registration', include('rest_auth.registration.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)