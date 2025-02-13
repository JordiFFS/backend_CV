from utils.utilsSerializers import *
from certificates.models import Certificates

folder_file = 'certificates'
full_folder = f'{MEDIA_ROOT}{folder_file}'


class CertificateSerializer(serializers.ModelSerializer):
    file_upload = FileSerializer(write_only=True)
    ext = serializers.CharField(read_only=True)
    ext_id = serializers.IntegerField()
    file = serializers.FileField(read_only=True)

    class Meta:
        model = Certificates
        fields = '__all__'

    def validate_file_upload(self, data):
        if not data.get("change"):
            raise serializers.ValidationError({"change": "Es requerido"})
        return data

    def validate(self, attrs):
        query = Certificates.objects.filter(
            Q(institute=attrs.get("institute")) &
            Q(title=attrs.get("title")) &
            Q(date=attrs.get("date")) &
            ~Q(pk=self.context.get("id", 0)))

        if query.exists():
            raise serializers.ValidationError({"certificate": "Este certificado ya existe"})
        return attrs


    def create(self, validated_data):
        if not os.path.exists(full_folder):
            os.makedirs(full_folder)
        file_upload = validated_data.pop('file_upload')
        file_name = randomstr(7)
        while True:
            if os.path.exists(f'{full_folder}/{file_name}.{file_upload.get("ext")}'):
                file_name = randomstr(7)
            else:
                break
        bites = base64.b64decode(file_upload.get('base64'))
        fh = open(f'{full_folder}/{file_name}.{file_upload.get("ext")}', 'wb')
        fh.write(bites)
        fh.close()
        validated_data["file"] = f'{folder_file}/{file_name}.{file_upload.get("ext")}'
        instance = Certificates(**validated_data)
        instance.save()
        return instance
