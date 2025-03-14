from utils.restFramework import *
from user_ext.api.serializers import WorkExperienceSerializers as serializer

class WorkExperiences(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serial = serializer.WorkExperienceSerializers(data = request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status.HTTP_201_CREATED)
            return Response(serial.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            query = serializer.WorkExperience.objects.filter(ext__user = request.user)
            serial = serializer.WorkExperienceSerializers(query, many = True)
            return Response(serial.data, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status.HTTP_500_INTERNAL_SERVER_ERROR)