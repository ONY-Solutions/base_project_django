from rest_framework import serializers
from src.application.auth_module.api.serializers.resource_serializers import ResourceSerializer

class ResourcesPayloadValidateSerializer(serializers.Serializer):
    herencia = serializers.BooleanField()
    resources = ResourceSerializer(many=True)

    def validate(self, data):
        for campo in ['herencia', 'resources']:
            if campo not in data:
                raise serializers.ValidationError(f"El campo '{campo}' es requerido")
            
        if not isinstance(data['resources'], list):
            raise serializers.ValidationError("El campo 'resources' debe ser una lista")
        
        if not len(data['resources']) > 0:
            raise serializers.ValidationError("El campo 'resources' no puede estar vacio")

        if not isinstance(data['herencia'], bool):
            raise serializers.ValidationError("El campo 'herencia' debe ser un booleano")
  
        return data
