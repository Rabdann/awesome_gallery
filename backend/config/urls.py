from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from app.views import (
    PictureViewSet,
    LoginAPIView,
    LogoutAPIView,
    RegisterAccountAPIView,
    DetailUserAPIView,
    DeletePicsAPIView
)


router = routers.SimpleRouter()
router.register("pictures", PictureViewSet, "picture")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("login/", LoginAPIView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
    path("registration/", RegisterAccountAPIView.as_view()),
    path("detail_user/", DetailUserAPIView.as_view()),
    path('delete_pics/', DeletePicsAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
