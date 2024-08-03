
from src.application.auth_module.api.repositories.persons_repository import PersonRepository

class AuthModuleRepositoryFactory:
    @staticmethod
    def get_person_repository():
        return PersonRepository()
