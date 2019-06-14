from rest_framework.routers import DefaultRouter
from croquis_listado.api.views import ReportesViewSet

app_name= 'croquis_litado_api'
router = DefaultRouter()
router.register(r'reportes',ReportesViewSet,base_name='reportes')

urlpatterns = []
urlpatterns += router.urls
