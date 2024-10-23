from rest_framework import serializers
from src.application.auth_module.api.serializers.resource_serializers import ResourceSerializer

class ResourcesPayloadValidateSerializer(serializers.Serializer):
    resources = ResourceSerializer(many=True)
    parent = serializers.CharField(required=False)

    def validate(self, data):
        for campo in ['resources']:
            if campo not in data:
                raise serializers.ValidationError(f"El campo '{campo}' es requerido")
            
        if not isinstance(data['resources'], list):
            raise serializers.ValidationError("El campo 'resources' debe ser una lista")
        
        if not len(data['resources']) > 0:
            raise serializers.ValidationError("El campo 'resources' no puede estar vacio")

        return data


class ResourceUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    path = serializers.CharField(required=False)
    icon = serializers.CharField(required=False)
    resource_parent = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    order = serializers.IntegerField(required=False)