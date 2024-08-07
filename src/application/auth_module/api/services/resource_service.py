from src.application.auth_module.api.repositories.resource_respository import (
    ResourceRepository,
)
from src.infrastructure.base_service import BaseService


class ResourceService(BaseService):

    def __init__(self, repository: ResourceRepository, serializer) -> None:
        self.repository = repository
        self.serializer = serializer

    def get_all(self):
        return self.serializer(self.repository.get_all(), many=True).data

    def get_by_id(self, pk):
        try:
            return self.serializer(self.repository.get_by_id(pk)).data
        except Exception as e:
            return e.args

    def create(self,payload):
        try:
            return self.serializer(self.repository.create(payload))
        except Exception as e:
            return e.args

    def update(self):
        pass

    def delete(self):
        pass
