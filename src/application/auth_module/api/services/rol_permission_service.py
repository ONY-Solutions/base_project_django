from src.infrastructure.base_service import BaseService
from src.interfaces.repository.base_repository import BaseRepository

class RolPermissionService(BaseService):

    model = "Rol_Permission"

    def __init__(self, repository: BaseRepository) -> None:
        self.repository = repository

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
