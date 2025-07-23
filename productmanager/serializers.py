from rest_framework import serializers

from .models import *

class WilayaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WilayaInfo
        fields = '__all__'