from rest_framework.viewsets import ModelViewSet

from core.models import Sessao
from core.serializers import SessaoSerializer


class SessaoViewSet(ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer
