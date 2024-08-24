from src.application.auth_module.api.repositories.user_repository import UserRepository
from src.infrastructure.base_service import BaseService


class UserService(BaseService):

    def __init__(self, repository: UserRepository, serializer) -> None:
        self.repository = repository
        self.serializer = serializer

    def get_all(self):
        pass

    def get_by_id(self, pk):
        return self.serializer(self.repository.get_by_id(pk)).data

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
