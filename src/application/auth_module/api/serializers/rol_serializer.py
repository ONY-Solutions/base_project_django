from rest_framework import serializers
from src.application.auth_module.models.rol import Rol


class RolValidateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
