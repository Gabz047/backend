from garagem.models.modelo import Modelo
from rest_framework.serializers import ModelSerializer


class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"