from rest_framework.serializers import ModelSerializer

from core.models import Carrinho


class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = "__all__"