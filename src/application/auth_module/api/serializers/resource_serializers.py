from rest_framework import serializers

class ResourceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    path = serializers.CharField()
    icon = serializers.CharField()
    resource_parent = serializers.IntegerField(read_only=True, required=False)