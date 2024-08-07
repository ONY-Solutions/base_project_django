from src.application.auth_module.api.repositories.rol_permission_repository import RolPermissionRepository
from src.domain.error_handlres import ErrorHandler
from src.infrastructure.base_service import BaseService
from django.db import transaction


class RolPermissionService(BaseService):

    model = "Rol_Permission"

    def __init__(self, repository: RolPermissionRepository, serializer) -> None:
        self.repository = repository
        self.serializer = serializer

    def get_all(self):
        return self.serializer(self.repository.get_all(), many=True).data

    def get_by_id(self, pk):
        try:
            return self.serializer(self.repository.get_by_id(pk)).data
        except Exception as e:
            return ErrorHandler.handle_error(e, self.model)

    @transaction.atomic
    def create(self, data):
        try:
            return self.serializer(self.repository.create(data)).data
        except Exception as e:
            return ErrorHandler.handle_error(e, self.model)

    @transaction.atomic
    def update(self, pk, data):
        try:
            return self.serializer(self.repository.update(pk, data)).data
        except Exception as e:
            return ErrorHandler.handle_error(e, self.model)

    @transaction.atomic
    def delete(self, pk):
        try:
            return self.serializer(self.repository.delete(pk)).data
        except Exception as e:
            return ErrorHandler.handle_error(e, self.model)
