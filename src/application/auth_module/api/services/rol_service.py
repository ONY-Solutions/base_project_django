from src.application.auth_module.api.repositories.rol_repository import RolRepository
from src.infrastructure.base_service import BaseService

class PersonService(BaseService):

    def __init__(self, repository: RolRepository, serializer) -> None:
        self.repository = repository
        self.serializer = serializer

    def get_all(self):
        return self.serializer(self.repository.get_all(), many=True).data

    def get_by_id(self, pk):
        try:
            return self.serializer(self.repository.get_by_id(pk)).data
        except Exception as e:
            return e.args

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
