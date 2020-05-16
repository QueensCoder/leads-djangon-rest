from rest_framework import serializers
from .models import Pets


class PetSerializer(serializers.Serializer):
    class Meta:
        model = Pets
        fields = ['name', 'age']
