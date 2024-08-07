

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from src.application.auth_module.api.views.permission.view import PermissionView

router = DefaultRouter()
router.register(r'permission', PermissionView, basename='permission')

urlpatterns = [
    path('', include(router.urls))
]
