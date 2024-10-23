from src.application.auth_module.api.repositories.resource_respository import (
    ResourceRepository,
)
from src.infrastructure.base_service import BaseService
from config.core.constants.response_messages import ResponseMessages
from django.db.models import Q

class ResourceService(BaseService):

    model = "Resource"

    def __init__(self, repository: ResourceRepository, serializer) -> None:
        self.repository = repository
        self.serializer = serializer

    def get_all(self):
        return self.serializer(self.repository.get_all(), many=True).data

    def get_by_id(self, pk):
        return self.serializer(self.repository.get_by_id(pk)).data

    def create(self, payload):
        path_or_id = payload.get("parent",None)
        resources_data = payload['resources']
        resources_list = []
        response = ResponseMessages.CREATED
        
        if path_or_id:
            queryset = self.repository.filter_custom(Q(id=path_or_id) | Q(path=path_or_id)).first()
            
            for resource_data in resources_data:
                path = resource_data.get("path", None)
                name = resource_data.get("name", None)
                icon = resource_data.get("icon", "")

                if path is not None:
                    model = self.repository.Model(
                            path=path,
                            resource_parent_id= queryset.pk,
                            name=name,
                            icon=icon
                        )
                    resources_list.append(model)
            response = self.serializer(resources_list,many=True).data
            self.repository.bulk_create(resources_list)  
        else:
            resources_created = []
            for resource_data in resources_data:
                path = resource_data.get("path", None)
                name = resource_data.get("name", None)
                icon = resource_data.get("icon", "")

                if path is not None:
                    dataValue = {
                            "path":path,
                            "name":name,
                            "icon":icon
                        }
         
                    instance = self.repository.create(dataValue)
                    resources_created.append(instance)
            response = self.serializer(resources_created,many=True).data
        return response

    def update(self, pk, payload):
        return self.serializer(self.repository.update(pk, payload), partial=True).data

    def delete(self, pk):
        return self.serializer(self.repository.delete(pk)).data
