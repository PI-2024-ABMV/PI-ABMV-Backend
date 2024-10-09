from rest_framework.serializers import ModelSerializer

from core.models import Assento

class AssentoSerializer(ModelSerializer):
    class Meta:
        model = Assento
        fields = '__all__'