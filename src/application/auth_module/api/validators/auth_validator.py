from rest_framework import serializers
from django.contrib.auth import authenticate

class AuthValidator(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    
    def validate(self, attrs):
        user = authenticate(**attrs)
    
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials Passed.")