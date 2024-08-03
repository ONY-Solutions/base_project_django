from rest_framework import serializers
from application.auth_module.models import User
from application.auth_module.api.serializers.person_serializers import PersonSerializer

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    person = PersonSerializer(read_only=True)
    # roles = serializers.EmailField(read_only=True)
    
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
