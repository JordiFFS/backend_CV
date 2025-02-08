from utils.restFramework import *
from certificates.api.serializers import CertificatesSerializers as serializer


class NewCertificate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serial = serializer.CertificateSerializer(data=request.data, context={'id': 0, 'request': request})
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status.HTTP_201_CREATED)
            return Response(serial.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            query = serializer.Certificates.objects.filter(ext__user=request.user)
            serial = serializer.CertificateSerializer(query, many=True, context={'request': request})
            return Response(serial.data)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateCertificate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            query = serializer.Certificates.objects.get(id = id)
            if serializer.os.path.exists(f'{serializer.MEDIA_ROOT}{query.file.name}'):
                serializer.os.remove(f'{serializer.MEDIA_ROOT}{query.file.name}')

            query.delete()
            return Response("", status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
