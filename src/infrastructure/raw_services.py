from django.db import models

class RawServicesBase:    
    
    def delete_many_records(self,model: models.Model, *args, **kwargs):
        model.objects.filter(**kwargs).delete()