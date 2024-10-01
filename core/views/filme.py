from rest_framework.viewsets import ModelViewSet

from core.models import Filme
from core.serializers import FilmeSerializer


class FilmeViewSet(ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer