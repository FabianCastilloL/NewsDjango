from .models import Noticias
from rest_framework import serializers

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticias
        fields='__all__'
    