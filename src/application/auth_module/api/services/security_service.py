from src.application.auth_module.api.repositories.rol_repository import (
    RolRepository)
from src.application.auth_module.api.repositories.resource_respository import (
    ResourceRepository)
from src.application.auth_module.api.repositories.rol_resource_repository import (
    RolResourceRepository)
from src.application.auth_module.api.repositories.permission_repository import (
    PermissionRepository)
from src.application.auth_module.api.repositories.rol_permission_repository import RolPermissionRepository
from src.infrastructure.base_service import BaseService
from django.db.transaction import atomic

class SecurityService(BaseService):

    model = "RolResource"

    def __init__(self, rol_repository: RolRepository, resource_respository: ResourceRepository, rol_resource_repository: RolResourceRepository, permission_repository: PermissionRepository,rol_permission_repository: RolPermissionRepository, serializer) -> None:
        self.rol_repository = rol_repository
        self.resource_respository = resource_respository
        self.rol_resource_repository = rol_resource_repository
        self.permission_repository = permission_repository
        self.rol_permission_repository = rol_permission_repository
        self.serializer = serializer

    def getResourcesByRol(self, pk):
        rol = self.rol_repository.get_by_id(pk)
        resources = self.resource_respository.filter_custom(rol=rol.pk)
        responseValue = {"rol": rol, "resources": resources}
        return self.serializer(responseValue).data

    @atomic
    def updateResourcesByRol(self, pk, data):
        rol = self.rol_repository.get_by_id(pk)
        resources = self.resource_respository.filter_custom(rol=rol.pk)
        current_resources_ids = set(resources.values_list('id', flat=True))
        payload_resources_ids = set(data)

        resources_to_add = payload_resources_ids - current_resources_ids
        resources_to_remove = current_resources_ids - resources_to_add
        
        for resource in resources_to_add:
            body = {"rol_id": rol.pk, "resource_id": resource}
            self.rol_resource_repository.create(body)
            
        for resource in resources_to_remove:
            x = self.rol_resource_repository.filter_custom(resource_id=resource).first()
            if x is not None:
                self.rol_resource_repository.delete(x.pk)

        return self.serializer({"OK": "OK"}).data

    def getPermissionsByRol(self, pk):
        rol = self.rol_repository.get_by_id(pk)
        permission = self.permission_repository.filter_custom(rol=rol.pk)    
        response_value = {"rol": rol, "permission": permission}
        return self.serializer(response_value).data

    @atomic
    def updatePermissionByRol(self, pk, data):
        rol = self.rol_repository.get_by_id(pk)
        permissions = self.permission_repository.filter_custom(rol=rol.pk)
        current_permissions_ids = set(permissions.values_list('id', flat=True))
        payload_permissions_ids = set(data)

        permissions_to_add = payload_permissions_ids - current_permissions_ids
        permissions_to_remove = current_permissions_ids.symmetric_difference(payload_permissions_ids)

        for permission in permissions_to_remove:
            x = self.rol_permission_repository.filter_custom(permission_id=permission).first()
            if x is not None:
                x.delete()

        for permission in permissions_to_add:
            body = {"rol_id": rol.pk, "permission_id": permission}
            self.rol_permission_repository.create(body)

        return self.serializer({"OK": "OK"}).data

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