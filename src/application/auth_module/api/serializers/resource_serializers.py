from rest_framework import serializers

class ResourceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    path = serializers.CharField()
    resource_parent = serializers.PrimaryKeyRelatedField(read_only=True, required=False)