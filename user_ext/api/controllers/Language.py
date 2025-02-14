from utils.restFramework import *
from user_ext.api.serializers import LanguageSerializers as serializer

class Languages(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serial = serializer.LanguageSerializers(data = request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status.HTTP_201_CREATED)
            return Response(serial.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            query = serializer.Language.objects.filter(ext__user = request.user)
            serial = serializer.LanguageSerializers(query, many = True)
            return Response(serial.data, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateLanguage(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            query = serializer.Language.objects.get(id = id)
            query.delete()
            return Response("", status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)