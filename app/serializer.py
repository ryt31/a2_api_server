from rest_framework import serializers
from .models import Information


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ('id', 'date', 'url', 'content', 'created_at')
