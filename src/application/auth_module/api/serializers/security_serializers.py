from rest_framework import serializers
from src.application.auth_module.api.serializers.rol_serializer import RolValidateSerializer
from src.application.auth_module.api.serializers.resource_serializers import ResourceSerializer
from src.application.auth_module.api.serializers.permission_serializer import PermissionValidateSerializer


class ResourcesByRolSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rol = RolValidateSerializer(read_only=True)
    resources = ResourceSerializer(many=True, read_only=True)

class PermissionByRolSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rol = RolValidateSerializer(read_only=True)
    permission = PermissionValidateSerializer(many=True, read_only=True)