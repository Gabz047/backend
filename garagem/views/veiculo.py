from rest_framework.viewsets import ModelViewSet
from garagem.models.veiculo import Veiculo
from garagem.serializers.veiculo import VeiculoSerializer, VeiculoListSerializer, VeiculoDetailSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        if self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer