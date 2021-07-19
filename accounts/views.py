from django.shortcuts import render
from .serializers import (RegisterUserSerializers)
from .authentication import (FirebaseAuthenticationToRegister)
from .permissions import (FireBaseIsAuthenticatedToRegister)
# Create your views here.

from rest_framework import generics

class ResgiterUserView(generics.CreateAPIView):
    authentication_classes = (FirebaseAuthenticationToRegister,)
    permission_classes = (FireBaseIsAuthenticatedToRegister,)
    serializer_class = (RegisterUserSerializers)