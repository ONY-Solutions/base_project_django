from rest_framework import serializers
from src.application.auth_module.models import User
from src.application.auth_module.api.serializers.person_serializers import PersonSerializer
from src.application.auth_module.api.serializers.rol_serializer import RolValidateSerializer
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    person = PersonSerializer(read_only=True)
    roles = RolValidateSerializer(read_only=True, many=True)
    
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
