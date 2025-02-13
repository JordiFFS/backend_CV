from utils.utilsSerializers import *
from user_ext.models import Hobbys


class HobbysSerializers(serializers.ModelSerializer):
    ext = serializers.CharField(read_only=True)
    ext_id = serializers.IntegerField()

    class Meta:
        model = Hobbys
        fields = '__all__'