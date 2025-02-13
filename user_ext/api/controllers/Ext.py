
from utils.restFramework import *
from user_ext.api.serializers import ExtSerializers as serializer

class Register(APIView):
    '''authentication_classes = [
        TokenAuthentication
    ]
    permission_classes = [
        IsAuthenticated
    ]'''
    def post(self,request):
        try:
            serial = serializer.CreateExtSerializer(data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status.HTTP_201_CREATED)
            return Response(serial.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class Login(APIView):
    def post(self, request):
        try:
            serial = serializer.LoginSerializer(data=request.data, context={'request':request})
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status.HTTP_201_CREATED)
            return Response(serial.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class TokenVerify(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            query = serializer.Token.objects.get(user = request.user)
            print(query)
            serial = serializer.TokenRestore(query, context={'request':request})
            return Response (serial.data)
        except Exception as e:
            print(e)
            return Response({"error": [str(e)]}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChangeImage(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        try:
            query = serializer.Ext.objects.get(user = request.user)
            serial = serializer.ControlImg(instance=query, data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status.HTTP_200_OK)
            return Response(serial.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            print(e)
            return Response({"error": [str(e)]}, status.HTTP_500_INTERNAL_SERVER_ERROR)


