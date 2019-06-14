from croquis_listado.models import Zona ,Distrito ,Departamento, Provincia
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from croquis_listado.api.serializers import ZonaSerializer
from rest_framework.response import Response
from django.db.models import Sum,Count,Avg,Aggregate,F,FloatField
from django.db.models.functions import Cast
from rest_framework.permissions import IsAuthenticated
class ReportesViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer

    @action(detail=False,methods=['get'],url_path='reporte_avance_segmentacion/(?P<nivel>[0-9]{1})/?(?P<codigo>[0-9]{2,6})?')
    def reporte_avance_segmentacion(self,request,*args,**kwargs):
        #nivel=request.GET.get('nivel')
        #nivel=int(nivel) if nivel is not None else 1
#
        #codigo=request.GET.get('codigo')
        #codigo = codigo if codigo is not  None else ''

        nivel=kwargs.get('nivel')
        nivel=int(nivel) if nivel is not None else 0

        codigo=kwargs.get('codigo')
        codigo = codigo if codigo is not  None else ''
        res=[]

        filters ={}


        if nivel ==0:
            res = Departamento.objects.annotate(cant_zona_marco=F('cant_zonas_marco'),cant_zona_segm=F('cant_zonas_segm'),codigo=F('ccdd'),descripcion=F('nombdep') ).values('codigo','descripcion','cant_zona_marco','cant_zona_segm','porcent_segm')

        elif nivel ==1:
            if codigo !='':
                filters['ccdd']=codigo
            res = Provincia.objects.filter(**filters).annotate(cant_zona_marco=F('cant_zonas_marco'),
                                            cant_zona_segm=F('cant_zonas_segm'), codigo=F('codprov'),
                                            descripcion=F('nombprov')).values('codigo', 'descripcion', 'cant_zona_marco',
                                                                             'cant_zona_segm','porcent_segm')


        elif nivel ==2:
            if codigo !='':
                filters['codprov']=codigo
            res = Distrito.objects.filter(**filters).annotate(cant_zona_marco=Sum('cant_zonas_marco'),
                                            cant_zona_segm=Sum('cant_zonas_segm'), codigo=F('ubigeo'),
                                            descripcion=F('nombdist')).values('codigo', 'descripcion', 'cant_zona_marco',
                                                                             'cant_zona_segm','porcent_segm')

        elif nivel==3:
            if codigo !='':
                filters['ubigeo']=codigo
            res= Zona.objects.filter(**filters).annotate(codigo=F('idzona'),descripcion=F('zona'),cant_zona_marco=Count('zona'),cant_zona_segm=F('flag_segm')).values('codigo','descripcion','cant_zona_marco','cant_zona_segm')
                                                                                                                                                                      #,'porcent_segm')




        return Response(res)



