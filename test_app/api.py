from .models import TestLead
from rest_framework import viewsets, permissions
from .serializers import TestSerialzer


# view set

class TestViewSet(viewsets.ModelViewSet):
    queryset = TestLead.objects.all()
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    serializer_class = TestSerialzer
