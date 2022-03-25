from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers
from landlords.views import LandlordViewSet

from members.views import MemberViewSet
from properties.views import PropertyViewSet

r = routers.DefaultRouter()
r.register(r"members", MemberViewSet)
r.register(r"properties", PropertyViewSet)
r.register(r"landlords", LandlordViewSet)

urlpatterns = [
    path("api/", include(r.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]
