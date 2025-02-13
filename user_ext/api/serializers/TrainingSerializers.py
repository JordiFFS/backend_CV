from utils.utilsSerializers import *
from user_ext.models import Training

class TrainingSerializer(serializers.ModelSerializer):
    ext = serializers.CharField(read_only=True)
    ext_id = serializers.IntegerField()

    class Meta:
        model = Training
        fields = '__all__'
