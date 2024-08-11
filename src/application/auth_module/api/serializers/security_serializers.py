from rest_framework import serializers
from src.application.auth_module.api.serializers.rol_serializer import RolValidateSerializer
from src.application.auth_module.api.serializers.resource_serializers import ResourceSerializer

class ResourcesByRolSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rol = RolValidateSerializer(read_only=True)
    resources = ResourceSerializer(many=True, read_only=True)

