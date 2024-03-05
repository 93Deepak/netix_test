from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Sensor, SensorData
from .serializers import SensorSerializer, SensorDataSerializer, SensorDataCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class SensorViewSet(viewsets.ModelViewSet):
    """
        Viewset to Create, Read, Update or Delete Sensor Record from DB
        Permitted to Authenticated users only
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

class SensorDataViewSet(viewsets.ModelViewSet):
    """
        Viewset to Create, Read, Update or Delete Sensor Record from DB
        Permitted to Authenticated users only
    """
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def create(self, request, *args, **kwargs):
        """
            This method creates new sensordata
            Permitted to Authenticated users only
        """
        serializer = SensorDataCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TokenCreateView(viewsets.ViewSet):
    """ 
        Token Create view to create an access token and refresh token for the given user credentials
        this token is used as Bearer token for authentication and accessing the APIs
        The token is Valid for 24 hours starting from its creation time
        after that user needs to provide refresh token to get a new access token and refresh token
        """
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
        else:
            return Response({'error': 'Username and password are required'}, status=400)