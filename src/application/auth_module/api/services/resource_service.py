from src.application.auth_module.api.repositories.resource_respository import (
    ResourceRepository,
)
from src.infrastructure.base_service import BaseService
from src.domain.error_handlres import ErrorHandler
from config.core.constants.response_messages import ResponseMessages


class ResourceService(BaseService):

    model = "Resource"

    def __init__(self, repository: ResourceRepository, serializer) -> None:
        self.repository = repository
        self.serializer = serializer

    def get_all(self):
        return self.serializer(self.repository.get_all(), many=True).data

    def get_by_id(self, pk):
        try:
            return self.serializer(self.repository.get_by_id(pk)).data
        except Exception as e:
            return ErrorHandler.handle_error(e, self.model)

    def create(self, payload):
        try:
            herencia = payload['herencia']
            resources_data = payload['resources']
            
            response = ResponseMessages.CREATED
            
            if herencia:
                resource_data = resources_data[0]
                path = resource_data.get("path", None)
                resource_parent = resource_data.get("resource_parent", None)
                name = resource_data.get("name", None)
                icon = resource_data.get("icon", "")

                if path is not None and resource_parent is not None:
                    dataValue = {
                        "path":path,
                        "resource_parent_id": resource_parent,
                        "name":name,
                        "icon":icon
                    }
                    response = self.serializer(self.repository.create(dataValue)).data
            else:
                resource_parent = None
                resources_created = []
                for resource_data in resources_data:
                    path = resource_data.get("path", None)
                    name = resource_data.get("name", None)
                    icon = resource_data.get("icon", "")

                    if path is not None:
                        dataValue = {
                            "path":path,
                            "resource_parent_id": resource_parent,
                            "name":name,
                            "icon":icon
                        }
         
                        instance = self.repository.create(dataValue)
                        resource_parent = instance.pk
                        resources_created.append(self.serializer(instance).data)
                response = resources_created
            return response
        except Exception as e:
            return ErrorHandler.handle_error(e, self.model)

    def update(self, pk, payload):
        try:
            return self.serializer(self.repository.update(pk, payload)).data
        except Exception as e:
            return ErrorHandler.handle_error(e, self.model)

    def delete(self, pk):
        try:
            return self.serializer(self.repository.delete(pk)).data
        except Exception as e:
            return ErrorHandler.handle_error(e, self.model)
