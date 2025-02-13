from utils.utilsSerializers import *
from user_ext.models import WorkExperience

class WorkExperienceSerializers(serializers.ModelSerializer):
    ext = serializers.CharField(read_only=True)
    ext_id = serializers.IntegerField()

    class Meta:
        model = WorkExperience
        fields = '__all__'