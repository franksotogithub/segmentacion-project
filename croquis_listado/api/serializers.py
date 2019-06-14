from rest_framework import serializers
from croquis_listado.models import Zona

class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = '__all__'

