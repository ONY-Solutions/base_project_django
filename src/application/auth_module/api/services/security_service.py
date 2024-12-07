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

    def __init__(self, rol_repository: RolRepository, resource_respository: ResourceRepository, rol_resource_repository: RolResourceRepository, permission_repository: PermissionRepository,rol_permission_repository: RolPermissionRepository, user_repository: UserRepository ,serializer) -> None:
        self.rol_repository = rol_repository
        self.resource_respository = resource_respository
        self.rol_resource_repository = rol_resource_repository
        self.permission_repository = permission_repository
        self.rol_permission_repository = rol_permission_repository
        self.user_repository = user_repository
        self.serializer = serializer

    def getResourcesByRol(self, pk):
        rol = self.rol_repository.get_by_id(pk)
        resources = self.resource_respository.filter_custom(rol=pk)
        responseValue = {"rol": rol, "resources": resources}
        return self.serializer(responseValue).data

    @atomic
    def updateResourcesByRol(self, pk, data):
        rol = self.rol_repository.get_by_id(pk)
        resources = self.resource_respository.filter_custom(rol=rol.pk).values_list('id', flat=True)
        current_resources_ids = set(resources)
        payload_resources_ids = set(data)

        resources_to_add = payload_resources_ids - current_resources_ids
        resources_to_remove = current_resources_ids.difference(payload_resources_ids)
        
        """ DELETE RECORDS """
        self.delete_many_records(model=self.rol_resource_repository.Model, resource_id__in=list(resources_to_remove))
        
        for resource in resources_to_add:
            body = {"rol": rol, "resource_id": resource}
            self.rol_resource_repository.create(body)

        return self.serializer({"OK": "OK"}).data

    def getPermissionsByRol(self, pk):
        rol = self.rol_repository.get_by_id(pk)
        permission = self.permission_repository.filter_custom(rol=rol.pk)    
        response_value = {"rol": rol, "permission": permission}
        return self.serializer(response_value).data

    @atomic
    def updatePermissionByRol(self, pk, data):
        rol = self.rol_repository.get_by_id(pk)
        permissions = self.permission_repository.filter_custom(rol=rol.pk).values_list('id', flat=True)
        current_permissions_ids = set(permissions)
        payload_permissions_ids = set(data)

        permissions_to_add = payload_permissions_ids - current_permissions_ids
        permissions_to_remove = current_permissions_ids.difference(payload_permissions_ids)
        
        """ DELETE RECORDS """
        self.delete_many_records(model=self.rol_permission_repository.Model, permission_id__in=list(permissions_to_remove))

        for permission in permissions_to_add:
            body = {"rol": rol, "permission_id": permission}
            self.rol_permission_repository.create(body)

        return self.serializer({"OK": "OK"}).data

    def getAllRolesByUser(self, user_id):
        roles  = self.rol_repository.filter_custom(user_roles=user_id)
        return self.serializer(roles, many=True).data
    
    @atomic
    def asingUserRol(self, pk, data):
        
        user = self.user_repository.get_by_id(pk)
        user.roles.set(data)

        return self.serializer(user).data

    def getAllResourcesByRol(self, **kwargs):
        resources = self.resource_respository.complex_filters(**kwargs).order_by("-order")
        return self.serializer(resources,many=True).data

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
