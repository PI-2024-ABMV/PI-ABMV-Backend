from rest_framework.serializers import ModelSerializer

from core.models import Sessao


class SessaoSerializer(ModelSerializer):
    class Meta:
        model = Sessao
        fields = '__all__'