from rest_framework_simplejwt import views

from api.views.user_views.serializer import (
    CustomTokenObtainPairSerializer,
    CustomVerifySerializer
)


class TokenObtainPairView(views.TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TokenRefreshView(views.TokenRefreshView):
    pass


class TokenVerifyView(views.TokenVerifyView):
    serializer_class = CustomVerifySerializer
