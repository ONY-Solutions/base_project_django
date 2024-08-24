from rest_framework import serializers


class RolResourceValidate(serializers.Serializer):
    resources = serializers.ListField(child=serializers.IntegerField())


class RolPermissionsValidate(serializers.Serializer):
    permissions = serializers.ListField(child=serializers.IntegerField())
    
class UserRolValidator(serializers.Serializer):
    roles = serializers.ListField(child=serializers.IntegerField())