from usuarios.api.serializers import UsuarioSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UsuarioSerializer(user, context={'request': request}).data
    }