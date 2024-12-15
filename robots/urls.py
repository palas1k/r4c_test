from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from robots.views import RobotCreateView

urlpatterns = [
    path('create', RobotCreateView.as_view(), name='robot_create'),
]
