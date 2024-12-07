from django.db import models

class RawServicesBase:    
    
    def records_to_delete_by_bulk(self,model: models.Model, *args, **kwargs):
        
        """ Don't logic delete """
        model.objects.filter(**kwargs).delete()