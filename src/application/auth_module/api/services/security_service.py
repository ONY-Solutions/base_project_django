from src.application.auth_module.api.repositories.rol_repository import (
    RolRepository)
from src.application.auth_module.api.repositories.resource_respository import (
    ResourceRepository)
from src.application.auth_module.api.repositories.rol_resource_repository import (
    RolResourceRepository)
from src.application.auth_module.api.repositories.permission_repository import (
    PermissionRepository)
from src.application.auth_module.api.repositories.user_repository import UserRepository
from src.application.auth_module.api.repositories.rol_permission_repository import RolPermissionRepository
from src.infrastructure.base_service import BaseService
from src.infrastructure.raw_services import RawServicesBase
from django.db.transaction import atomic

class SecurityService(BaseService, RawServicesBase):

    model = "SECURITY"

    def __init__(self, rol_repository: RolRepository, resource_respository: ResourceRepository, rol_resource_repository: RolResourceRepository, permission_repository: PermissionRepository,rol_permission_repository: RolPermissionRepository, user_repository: UserRepository) -> None:
        self.rol_repository = rol_repository
        self.resource_respository = resource_respository
        self.rol_resource_repository = rol_resource_repository
        self.permission_repository = permission_repository
        self.rol_permission_repository = rol_permission_repository
        self.user_repository = user_repository

    def getResourcesByRol(self, pk):
        rol = self.rol_repository.get_by_id(pk)
        resources = self.resource_respository.filter_custom(rol=pk)
        responseValue = {"rol": rol, "resources": resources}
        return responseValue

    @atomic
    def updateResourcesByRol(self, pk, data):
        rol = self.rol_repository.get_by_id(pk)
        resources = self.resource_respository.filter_custom(rol=rol).values_list('id', flat=True)
        current_resources_ids = set(resources)
        payload_resources_ids = set(data)

        resources_to_add = payload_resources_ids - current_resources_ids
        resources_to_remove = current_resources_ids.difference(payload_resources_ids)
        
        
        resources_to_response = []
        
        """ DELETE RECORDS """
        self.records_to_delete_by_bulk(model=self.rol_resource_repository.Model, resource_id__in=list(resources_to_remove))
        
        for resource in resources_to_add:
            body = {"rol": rol, "resource_id": resource}
            resources_to_response.append(self.rol_resource_repository.create(body))

        return resources_to_response

    def getPermissionsByRol(self, pk):
        rol = self.rol_repository.get_by_id(pk)
        permission = self.permission_repository.filter_custom(rol=rol.pk)    
        response_value = {"rol": rol, "permission": permission}
        return response_value

    @atomic
    def updatePermissionByRol(self, pk, data):
        rol = self.rol_repository.get_by_id(pk)
        permissions = self.permission_repository.filter_custom(rol=rol).values_list('id', flat=True)
        current_permissions_ids = set(permissions)
        payload_permissions_ids = set(data)

        permissions_to_add = payload_permissions_ids - current_permissions_ids
        permissions_to_remove = current_permissions_ids.difference(payload_permissions_ids)
        
        """ DELETE RECORDS """
        self.records_to_delete_by_bulk(model=self.rol_permission_repository.Model, permission_id__in=list(permissions_to_remove))

        permissions_to_response = []

        for permission in permissions_to_add:
            body = {"rol": rol, "permission_id": permission}
            permissions_to_response.append(self.rol_permission_repository.create(body))

        return permissions_to_response

    def getAllRolesByUser(self, user_id):
        roles  = self.rol_repository.filter_custom(user_roles=user_id)
        return roles
    
    @atomic
    def asingUserRol(self, pk, data):
        
        user = self.user_repository.get_by_id(pk)
        user.roles.set(data)

        return user

    def getAllResourcesByRol(self, **kwargs):
        resources = self.resource_respository.complex_filters(**kwargs).order_by("-order")
        return resources

    def get_all(self):
        pass

    def get_by_id(self, pk):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
