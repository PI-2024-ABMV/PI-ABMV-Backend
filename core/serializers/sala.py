from rest_framework.serializers import ModelSerializer

from core.models import Sala


class SalaSerializer(ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'