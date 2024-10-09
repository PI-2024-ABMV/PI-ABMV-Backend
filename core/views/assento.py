from rest_framework.viewsets import ModelViewSet

from core.models import Assento
from core.serializers import AssentoSerializer


class AssentoViewSet(ModelViewSet):
    queryset = Assento.objects.all()
    serializer_class = AssentoSerializer
