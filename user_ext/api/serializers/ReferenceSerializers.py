from utils.utilsSerializers import *
from user_ext.models import Reference

class ReferenceSerializers(serializers.ModelSerializer):
    ext = serializers.CharField(read_only=True)
    ext_id = serializers.IntegerField()

    class Meta:
        model = Reference
        fields = '__all__'