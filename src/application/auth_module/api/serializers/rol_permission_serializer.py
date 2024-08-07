from rest_framework import serializers
from src.application.auth_module.api.serializers.rol_serializer import RolValidateSerializer
from src.application.auth_module.api.serializers.permission_serializer import PermissionValidateSerializer


class RolPermissionSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    rol = RolValidateSerializer()
    permission = PermissionValidateSerializer()
