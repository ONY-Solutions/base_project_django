import copy
from rest_framework import serializers
class BaseSerializer(serializers.Serializer):
    
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)

        original_fields = {name: field for name, field in self.fields.items()}
        
        self.fields.clear()
        
        class DataSerializer(serializers.Serializer):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for field_name, field in original_fields.items():
                    new_field = copy.deepcopy(field)
                    new_field.required = False
                    
                    if not hasattr(new_field, 'default'):
                        new_field.default = None

                    self.fields[field_name] = new_field
        
        
        self.fields["data"] = DataSerializer(required=False,)
        self.fields["status"] = serializers.IntegerField(required=False,)
        self.fields["method"] = serializers.CharField(required=False,)
        self.fields["url"] = serializers.CharField(required=False,)
        self.fields["errors"] = serializers.DictField(required=False, default=dict)
        
        