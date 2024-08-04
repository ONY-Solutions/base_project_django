from rest_framework import serializers
from src.application.auth_module.models.rol import Rol


class RolSerializerValidate(serializers.Serializer):
    name = serializers.CharField()
