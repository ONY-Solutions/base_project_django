from src.infrastructure.base_service import BaseService
from src.interfaces.repository.base_repository import BaseRepository

class RolService(BaseService):
    model = "Rol"

    def __init__(self, repository: BaseRepository) -> None:
        self.repository = repository

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
