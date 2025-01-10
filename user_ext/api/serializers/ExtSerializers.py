from utils.utilsSerializers import *
from user_ext.models import Ext, User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

class ExtUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ext
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if instance.image:
            if request:
                url = request.build_absolute_uri('/')[:-1]
                data['image']= f'{url}{instance.image.url}'
            else:
                data['image']= f'{instance.image.url}'
        else:
            if request:
                url = request.build_absolute_uri('/')[:-1]
                data['image'] = f'{url}/media/profile_pics/default.jpg'
            else:
                data['image'] = f'/media/profile_pics/default.jpg'
        return data


class UserSerializer(serializers.ModelSerializer):
    ext = ExtUserSerializer(many=False)
    class Meta:
        model = User
        fields = '__all__'

class CreateExtSerializer(serializers.Serializer):
    user = serializers.CharField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    email = serializers.EmailField(write_only=True)
    phone = serializers.CharField(min_length=10)
    gender = serializers.CharField(read_only=True)
    gender_id = serializers.IntegerField()
    levelStudy = serializers.CharField(read_only=True)
    levelStudy_id = serializers.IntegerField()
    professionalTitle = serializers.CharField(read_only=True)
    professionalTitle_id = serializers.IntegerField(allow_null=True)
    countryResidence = serializers.CharField(read_only=True)
    countryResidence_id = serializers.IntegerField()

    def validate_email(self, data):
        if User.objects.filter(Q(email=data) & ~Q(pk=self.context.get('id'))).exists():
            raise serializers.ValidationError(f'El correo {data} ya pertenece a una cuenta')
        return data



    def create(self, validated_data):
        print(validated_data.get("email"))
        user=User()
        user.username=validated_data.get('email')
        user.first_name=validated_data.get('first_name')
        user.last_name=validated_data.get('last_name')
        user.set_password(validated_data.get('password'))
        user.email=validated_data.get('email')
        user.save()

        ext=Ext()
        ext.user=user
        ext.gender_id = validated_data.get('gender_id')
        ext.levelStudy_id = validated_data.get('levelStudy_id')
        ext.professionalTitle_id = validated_data.get('professionalTitle_id')
        ext.countryResidence_id = validated_data.get('countryResidence_id')
        ext.phone=validated_data.get('phone')
        ext.save()

        return validated_data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    def validate(self, attrs):
        user = User.objects.filter(Q(email=attrs.get('email')))
        if user.exists():
            user=user.first()
            if check_password(attrs.get('password'), user.password):
                token = Token.objects.get_or_create(user=user)
                attrs['token'] = token[0]
                attrs['user'] = user
                return attrs
        raise serializers.ValidationError({'msg': 'El usuario o la contraseña son incorrectos'})

    def create(self, validated_data):
        return validated_data

class TokenRestore(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField()
    class Meta :
        model = Token
        fields = '__all__'