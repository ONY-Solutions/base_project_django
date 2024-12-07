from src.infrastructure.base_service import BaseService
from src.interfaces.repository.base_repository import BaseRepository

class PermissionService(BaseService):

    model = "Permission"

    def __init__(self, repository: BaseRepository, rol_repository: BaseRepository) -> None:
        self.repository = repository
        self.rol_repository = rol_repository

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
        rol_record = self.rol_repository.get_by_id(pk)
        return {"rol": rol_record, "permissions": self.repository.filter_by_rol(pk)}

