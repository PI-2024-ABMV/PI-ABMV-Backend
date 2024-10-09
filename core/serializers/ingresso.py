from rest_framework.serializers import ModelSerializer

from core.models import Ingresso


class IngressoSerializer(ModelSerializer):
    class Meta:
        model = Ingresso
        fields = '__all__'