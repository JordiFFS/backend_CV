from rest_framework import serializers
from DJcv_backend.settings import DIR, os, MEDIA_ROOT, MEDIA_URL
from django.db.models import Q, Max, Sum, Count

class FileSerializer(serializers.Serializer):
    base64 = serializers.CharField(required=False, allow_blank=True)
    ext = serializers.CharField(required=False, allow_blank=True)
    change = serializers.BooleanField()

    def validate(self, attrs):
        if attrs.get('change'):
            message = {}
            error = False
            if attrs.get('base64') is None or attrs.get('base64') == '':
                error = True
                message['base64'] = 'El campo base64 es requerido'
            if attrs.get('ext') is None or attrs.get('ext') == '':
                error = True
                message['ext'] = 'El campo ext es requerido'
            if error:
                raise serializers.ValidationError(message)
        return attrs

#convertir en json
def ModelCbx(model):
    listData = []
    for data in model:
        jdata = {
            'value': data.pk,
            'label': str(data)
        }
        listData.append(jdata)
    return listData