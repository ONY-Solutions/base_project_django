from rest_framework import serializers

class ResourceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    path = serializers.CharField(read_only=True)
    resource_parent = serializers.IntegerField(read_only=True)
    rol = serializers.IntegerField(read_only=True)