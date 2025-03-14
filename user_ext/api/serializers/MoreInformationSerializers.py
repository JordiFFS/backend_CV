from utils.utilsSerializers import *
from user_ext.models import MoreInformation

class MoreInformationSerializer(serializers.ModelSerializer):
    ext = serializers.CharField(read_only=True)
    ext_id = serializers.IntegerField()

    class Meta:
        model = MoreInformation
        fields = '__all__'