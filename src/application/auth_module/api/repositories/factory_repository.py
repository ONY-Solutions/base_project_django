from src.application.auth_module.api.repositories.persons_repository import (
    PersonRepository,
)
from src.application.auth_module.api.services.person_service import PersonService


class AuthModuleRepositoryFactory:

    @staticmethod
    def get_person_repository():
        return PersonRepository()

    @staticmethod
    def get_person_service(serializer):
        repository = AuthModuleRepositoryFactory.get_person_repository()
        return PersonService(repository, serializer)
