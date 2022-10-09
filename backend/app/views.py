from distutils.util import strtobool

from rest_framework import viewsets, generics, views, response, permissions
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout

from .models import Picture
from .serializers import (
    PictureSerializer,
    LoginSerializer,
    RegisterAccountSerializer,
    DetailUserSerializer,
)


class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = PictureSerializer

    def get_queryset(self):
        user = self.request.user
        default_filter_kwarg = {"owner": user}
        active = self.request.query_params.get("is_active")
        if active is not None:
            active = strtobool(active)
            default_filter_kwarg["is_active"] = active
        return Picture.objects.filter(**default_filter_kwarg)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.data.get("username"))
        check_pass = check_password(serializer.data.get("password"), user.password)
        if check_pass:
            login(request, user)
            return response.Response(serializer.data)
        return response.Response("Некоректный пароль", status=400)


class LogoutAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        return response.Response(logout(request))


class RegisterAccountAPIView(generics.CreateAPIView):
    serializer_class = RegisterAccountSerializer


class DetailUserAPIView(generics.RetrieveAPIView):
    serializer_class = DetailUserSerializer

    def get_object(self):
        obj = self.request.user
        return obj


class DeletePicsAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        Picture.objects.all().delete()
        return response.Response()
