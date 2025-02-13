from utils.utilsSerializers import *
from user_ext.models import Language


class LanguageSerializers(serializers.ModelSerializer):
    ext = serializers.CharField(read_only=True)
    ext_id = serializers.IntegerField()

    class Meta:
        model = Language
        fields = '__all__'