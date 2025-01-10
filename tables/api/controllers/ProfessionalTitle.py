from utils.restFramework import *
from tables.api.serializers import ProfessionalTitleSerializers as serializer

class ComboBoxProfessionalTitle(APIView):

    def get(self, request):
        try:
            query = serializer.ProfessionalTitle.objects.all()
            cbx = serializer.ModelCbx(query)
            return Response(cbx)
        except Exception as e:
            print(e)
            return Response({'Error', str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)