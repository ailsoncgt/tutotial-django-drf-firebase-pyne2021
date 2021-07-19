from rest_framework.permissions import BasePermission
from rest_framework import exceptions
from django.contrib.auth import get_user_model
from . import firebase_admin
from rest_framework.authentication import get_authorization_header

class FireBaseIsAuthenticated(BasePermission):

    keyword = 'Bearer'
    model = get_user_model()
    firebase = None
    request = None

    def has_permission(self, request, view):
        self.request = request
        firebase_auth = firebase_admin.get_auth()

        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None
        
        if len(auth) == 1:
            msg = 'Token inválido'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Token nao pode ter espacos'
            raise exceptions.AuthenticationFailed(msg)
        
        decoded_token = None
        try:
            decoded_token = firebase_auth.verify_id_token(auth[1])
        except Exception as e:
            msg = 'Algo deu errado, tente novamente'
            raise exceptions.AuthenticationFailed(msg)
        
        uid = decoded_token.get('uid')

        return self.check_user(uid, request)

    def check_user(self, key, request):
        try:
            user = self.model.objects.get(username=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Usuário nao cadastrado')
        
        if not user.is_active:
            raise exceptions.AuthenticationFailed('Usuario não ativo ou excluido')
        request.user = user
        return True

class FireBaseIsAuthenticatedToRegister(FireBaseIsAuthenticated):

    def check_user(self, key, request):
        return True