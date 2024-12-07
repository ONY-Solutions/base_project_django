from src.application.auth_module.api.repositories.rol_repository import RolRepository
from src.infrastructure.base_service import BaseService

class RolService(BaseService):
    model = "Rol"

    def __init__(self, repository: RolRepository, serializer) -> None:
        self.repository = repository
        self.serializer = serializer

    def get_all(self):
        return self.repository.get_all()
    
    def get_filter(self, **kwargs):
        return self.repository.filter_custom(kwargs)

    def get_by_id(self, pk):
        return self.repository.get_by_id(pk)

    def create(self, data):
        return self.repository.create(data)

    def update(self, pk, data):
        return self.repository.update(pk, data)
    
    def delete(self, pk):
        return self.repository.delete(pk)
