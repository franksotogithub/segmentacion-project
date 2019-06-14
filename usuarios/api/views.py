from django.contrib.auth import authenticate
from rest_framework.viewsets import ViewSet, ModelViewSet
from usuarios.models import Usuario
from usuarios.api.serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class UsuariosViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)

class AuthViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    @action(detail=False, methods=['post'])
    def login(self,request):

        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key ,'user':UsuarioSerializer(user, context={'request': request}).data},
                        status=HTTP_200_OK)