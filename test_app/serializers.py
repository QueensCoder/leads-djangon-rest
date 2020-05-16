from rest_framework import serializers
from test_app.models import TestLead


class TestSerialzer(serializers.ModelSerializer):
    class Meta:
        model = TestLead
        fields = '__all__'
