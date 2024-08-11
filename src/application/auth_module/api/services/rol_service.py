from src.application.auth_module.api.repositories.rol_repository import RolRepository
from src.infrastructure.base_service import BaseService

class RolService(BaseService):
    model = "Rol"

    def __init__(self, repository: RolRepository, serializer) -> None:
        self.repository = repository
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
