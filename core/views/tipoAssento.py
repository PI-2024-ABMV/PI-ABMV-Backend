from rest_framework.viewsets import ModelViewSet

from core.models import TipoAssento
from core.serializers import TipoAssentoSerializer


class TipoAssentoViewSet(ModelViewSet):
    queryset = TipoAssento.objects.all()
    serializer_class = TipoAssentoSerializer