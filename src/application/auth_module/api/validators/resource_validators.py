from rest_framework import serializers
class ResourceCreateValidator(serializers.Serializer):

    def validate(self, data):
        for campo in ['name', 'path', 'resource_parent']:
            if campo not in data:
                raise serializers.ValidationError(f"El campo '{campo}' es requerido")
            
        if data['name'] == isinstance(data['name'], str):
            raise serializers.ValidationError("El campo 'name' debe ser de tipo 'str'")
        
        if data['path'] == isinstance(data['path'], str):
            raise serializers.ValidationError("El campo 'path' debe ser de tipo 'str'")
        
        if data['resource_parent'] == isinstance(data['resource_parent'], int):
            raise serializers.ValidationError("El campo 'resource_parent' debe ser de tipo 'int'")
        
        return data
