##db_________django_____api[json]______mobile && js framework

from rest_framework import serializers
from .models import job

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = '__all__'

