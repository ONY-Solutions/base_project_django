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
        return self.repository.get_all()

    def get_by_id(self, pk):
        return self.repository.get_by_id(pk)

    def create(self, payload):
        path_or_id = payload.get("parent",None)
        resources_data = payload.get('resources',[])
        resources_list = []
        response = ResponseMessages.CREATED
        queryset = self.repository.filter_custom(Q(id=path_or_id) | Q(path=path_or_id)).first()

        for resource_data in resources_data:
                path = resource_data.get("path", None)
                name = resource_data.get("name", None)
                icon = resource_data.get("icon", "")

                model = self.repository.Model(
                    path=path,
                    resource_parent=queryset,
                    name=name,
                    icon=icon
                )

                resources_list.append(model)
        self.repository.bulk_create(resources_list)

        return response

    def update(self, pk, payload):
        return self.repository.update(pk, payload)

    def delete(self, pk):
        return self.repository.delete(pk)
