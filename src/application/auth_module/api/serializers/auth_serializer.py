from rest_framework import serializers
from src.application.auth_module.api.serializers.user_serializers import UserSerializer
from src.application.auth_module.api.serializers.resource_serializers import ResourceSerializer
class AuthSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class SchemaTokenLogin(serializers.Serializer):
    access = serializers.CharField(read_only=True, required=False)
    refresh = serializers.CharField(read_only=True, required=False)


class SchemaResponseLogin(serializers.Serializer):
    token = SchemaTokenLogin(read_only=True, required=False,source= "s")


class SchemaResponseResources(serializers.Serializer):
    user = UserSerializer(read_only=True, required=False,source= "user_model")
    resources = ResourceSerializer(read_only=True, many=True, required=False,source= "user_resources")