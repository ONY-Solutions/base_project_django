from src.application.auth_module.api.repositories.persons_repository import (
    PersonRepository,
)
from src.application.auth_module.api.repositories.rol_repository import RolRepository
from src.application.auth_module.api.services.person_service import PersonService
from src.application.auth_module.api.services.rol_service import RolService
from src.application.auth_module.api.repositories.permission_repository import PermissionRepository
from src.application.auth_module.api.services.permission_service import PermissionService
from src.application.auth_module.api.services.rol_permission_service import RolPermissionService
from src.application.auth_module.api.repositories.rol_permission_repository import RolPermissionRepository


class AuthModuleRepositoryFactory:

    @staticmethod
    def get_person_repository():
        return PersonRepository()

    @staticmethod
    def get_rol_repository():
        return RolRepository()

    @staticmethod
    def get_permission_repository():
        return PermissionRepository()

    @staticmethod
    def get_rol_permission_repository():
        return RolPermissionRepository()

    @staticmethod
    def get_person_service(serializer):
        repository = AuthModuleRepositoryFactory.get_person_repository()
        return PersonService(repository, serializer)

    @staticmethod
    def get_rol_service(serializer):
        repository = AuthModuleRepositoryFactory.get_rol_repository()
        return RolService(repository, serializer)

    @staticmethod
    def get_permission_service(serializer):
        repository = AuthModuleRepositoryFactory.get_permission_repository()
        return PermissionService(repository, serializer)

    @staticmethod
    def get_rol_permission_service(serializer):
        repository = AuthModuleRepositoryFactory.get_rol_permission_repository()
        return RolPermissionService(repository, serializer)
