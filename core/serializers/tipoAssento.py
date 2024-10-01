from rest_framework.serializers import ModelSerializer

from core.models import TipoAssento


class TipoAssentoSerializer(ModelSerializer):
    class Meta:
        model = TipoAssento
        fields = '__all__'