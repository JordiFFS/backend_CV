from utils.restFramework import *
from user_ext.api.serializers import ReportsSerializers as serializer

class Reports(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            url = request.build_absolute_uri('/')[:-1]

            parametres = {
                "titulo_profecional": request.user.ext.professionalTitle.name,
                "fullname": request.user.get_full_name(),
                "email": request.user.email,
                "adress": "",
                "telefono": request.user.ext.phone,
                "cumple": "",
                "pais": request.user.ext.countryResidence.name,
                "red_social": "",
                "description": "",
                "ability": "",
                "level": "",
            }

            if request.user.ext.image:
                parametres["image"] = f'{url}{request.user.ext.image.url}'
            else:
                parametres["image"] = f'{url}/media/profile_pics/default.jpg'

            pdf = serializer.SendToJasper("fastcv", [{'Hoja de vida': 'hoja de vida'}], "pdf", parametres)
            print(pdf)
            return Response(pdf, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)