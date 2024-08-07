from rest_framework import serializers

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(read_only=True)
    identification = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)