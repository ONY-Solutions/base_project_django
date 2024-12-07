from rest_framework import serializers
from src.application.auth_module.api.serializers.rol_serializer import RolValidateSerializer
from src.application.auth_module.api.serializers.resource_serializers import ResourceSerializer


class RolResourceSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    rol = RolValidateSerializer()
    resource = ResourceSerializer()
