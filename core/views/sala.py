from rest_framework.viewsets import ModelViewSet

from core.models import Sala
from core.serializers import SalaSerializer


class SalaViewSet(ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer