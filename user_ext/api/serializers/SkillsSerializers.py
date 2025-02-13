from utils.utilsSerializers import *
from user_ext.models import Skills


class SkillsSerializers(serializers.ModelSerializer):
    ext = serializers.CharField(read_only=True)
    ext_id = serializers.IntegerField()

    class Meta:
        model = Skills
        fields = '__all__'