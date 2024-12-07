from rest_framework.viewsets import ViewSet

class BaseViewSet(ViewSet):
    
    def get_serializer_data(self, data_to_serializar, *args, **kwargs):
        serializer = self.get_serializer_class()
        return serializer(data_to_serializar, **kwargs)