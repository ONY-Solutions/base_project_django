from rest_framework import serializers

class Geeks(object):
    def __init__(self, dictionary):
        self.dict = dictionary

class BaseSerializer(serializers.Serializer):
    def __init__(self, instance=None, data=..., **kwargs):
        # Guardamos la definición original de los campos antes de llamar a super()
        original_fields = self._declared_fields.copy()
        
        # Limpiamos los campos declarados para que super() no los procese
        self._declared_fields.clear()
        
        # Llamamos al constructor padre
        super().__init__(instance, data, **kwargs)
        
        # Creamos un nuevo Serializer para contener los campos originales
        class DataSerializer(serializers.Serializer):
            pass
        
        # Agregamos todos los campos originales al DataSerializer

        
        fields = {"test": "test"}
        
        for name, field in original_fields.items():
            fields[name] = field

        # Definimos la estructura final del serializer
        self.fields['data'] = serializers.DictField(default=fields)
        self.fields['status'] = serializers.IntegerField(required=False)
        self.fields['method'] = serializers.CharField(required=False)
        self.fields['url'] = serializers.CharField(required=False)
        self.fields['errors'] = serializers.DictField(required=False, default=dict)
