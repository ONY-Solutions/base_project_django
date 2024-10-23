from src.application.auth_module.api.repositories.permission_repository import PermissionRepository
from src.infrastructure.base_service import BaseService
from src.application.auth_module.api.repositories.rol_repository import RolRepository


class PermissionService(BaseService):

    model = "Permission"

    def __init__(self, repository: PermissionRepository, rol_repository: RolRepository, serializer) -> None:
        self.repository = repository
        self.rol_repository = rol_repository
        self.serializer = serializer

    def get_all(self):
        return self.serializer(self.repository.get_all(), many=True).data

    def get_by_id(self, pk):
        return self.serializer(self.repository.get_by_id(pk)).data

    def create(self, data):
        return self.serializer(self.repository.create(data)).data

    def update(self, pk, data):
        return self.serializer(self.repository.update(pk, data)).data

    def delete(self, pk):
        return self.serializer(self.repository.delete(pk)).data

    def permission_by_rol(self, pk):
        rol_data = self.rol_repository.get_by_id(pk)
        return self.serializer({"rol": rol_data, "permissions": self.repository.filter_by_rol(pk)}).data

