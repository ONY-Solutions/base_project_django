

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from src.application.auth_module.api.views.rol_permission.view import RolPermissionView

router = DefaultRouter()
router.register(r'control/rol/permission', RolPermissionView,
                basename='rol-permission')

urlpatterns = [
    path('', include(router.urls))
]
