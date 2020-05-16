from .models import Pets
from .serializers import PetSerializer
from rest_framework import viewsets, permissions


class PetViewSet(viewsets.ViewSet):
    query_set = Pets.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PetSerializer
