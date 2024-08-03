from rest_framework import serializers
from src.application.auth_module.models import Person

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(read_only=True)
    identification = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    
class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
