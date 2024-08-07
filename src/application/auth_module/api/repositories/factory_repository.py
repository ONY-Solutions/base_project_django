from src.application.auth_module.api.repositories.persons_repository import (
    PersonRepository,
)
from src.application.auth_module.api.repositories.rol_repository import RolRepository
from src.application.auth_module.api.repositories.resource_respository import ResourceRepository
from src.application.auth_module.api.services.person_service import PersonService
from src.application.auth_module.api.services.resource_service import ResourceService



class AuthModuleRepositoryFactory:

    @staticmethod
    def get_person_repository():
        return PersonRepository()

    @staticmethod
    def get_rol_repository():
        return RolRepository()

    @staticmethod
    def get_resource_repository():
        return ResourceRepository()

    @staticmethod
    def get_person_service(serializer):
        repository = AuthModuleRepositoryFactory.get_person_repository()
        return PersonService(repository, serializer)

    @staticmethod
    def get_rol_service(serializer):
        repository = AuthModuleRepositoryFactory.get_rol_repository()
        return PersonService(repository, serializer)

    @staticmethod
    def get_resource_service(serializer):
        repository = AuthModuleRepositoryFactory.get_resource_repository()
        return ResourceService(repository, serializer)
