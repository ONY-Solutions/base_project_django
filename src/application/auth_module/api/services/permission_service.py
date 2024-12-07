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
        return self.repository.get_all()

    def get_by_id(self, pk):
        return self.repository.get_by_id(pk)

    def create(self, data):
        return self.repository.create(data)

    def update(self, pk, data):
        return self.repository.update(pk, data)

    def delete(self, pk):
        return self.repository.delete(pk)

    def permission_by_rol(self, pk):
        rol_data = self.rol_repository.get_by_id(pk)
        return {"rol": rol_data, "permissions": self.repository.filter_by_rol(pk)}

