from src.application.auth_module.api.repositories.resource_respository import (
    ResourceRepository,
)
from src.infrastructure.base_service import BaseService
from src.domain.error_handlres import ErrorHandler


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
        # except ObjectDoesNotExist as e:
        #     return ErrorHandler.handle_error(e, self.model)
        except Exception as e:
            return ErrorHandler.handle_error(e, self.model)

    def create(self, payload):
        try:
            return self.serializer(self.repository.create(payload)).data
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
