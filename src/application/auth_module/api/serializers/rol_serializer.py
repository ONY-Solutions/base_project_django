from rest_framework import serializers
from src.application.auth_module.models.rol import Rol


class RolValidateSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField(read_only=True)
