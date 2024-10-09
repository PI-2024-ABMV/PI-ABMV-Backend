from rest_framework.viewsets import ModelViewSet

from core.models import Ingresso
from core.serializers import IngressoSerializer


class IngressoViewSet(ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer