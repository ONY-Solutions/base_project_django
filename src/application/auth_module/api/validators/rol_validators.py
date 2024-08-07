from rest_framework import serializers

class RolPermissionValidator(serializers.Serializer):
    rol = serializers.IntegerField()
    permission = serializers.IntegerField()
    
    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        
        return {
            "rol_id": representation["rol"],
            "permission_id": representation["permission"]
        }
        
        