from rest_framework import serializers
from src.application.auth_module.models.rol import Rol


class PermissionValidateSerializer(serializers.Serializer):
    name = serializers.CharField()
    path = serializers.CharField()
    method = serializers.CharField()
    id = serializers.IntegerField(read_only=True)


class PermissionUpdateValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    path = serializers.CharField(required=False)
    method = serializers.CharField(required=False)
