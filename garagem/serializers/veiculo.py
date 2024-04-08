from garagem.models.veiculo import Veiculo
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.models.image import Image
from uploader.serializers.image import ImageSerializer


class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "ano", "modelo", "descricao"]

class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1
        imagem = ImageSerializer(required=False)
    
class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
    imagem_attachment_key = SlugRelatedField(
        source='imagem',
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True
    )
    imagem = ImageSerializer(required=False, read_only=True)

