from src.application.auth_module.api.repositories.rol_repository import (
    RolRepository)
from src.application.auth_module.api.repositories.resource_respository import (
    ResourceRepository)
from src.application.auth_module.api.repositories.rol_resource_repository import (
    RolResourceRepository)
from src.infrastructure.base_service import BaseService


class SecurityService(BaseService):

    model = "RolResource"

    def __init__(self, rol_repository: RolRepository, resource_respository: ResourceRepository, rol_resource_repository: RolResourceRepository, serializer) -> None:
        self.rol_repository = rol_repository
        self.resource_respository = resource_respository
        self.rol_resource_repository = rol_resource_repository
        self.serializer = serializer

    def getResourcesByRol(self, pk):
        rol = self.rol_repository.get_by_id(pk)
        resources = self.resource_respository.filter_custom(rol=rol.pk)
        # self.rol_resource_repository.filter_custom(resource_id=resource).first()
        responseValue = {"rol": rol, "resources": resources}
        return self.serializer(responseValue).data

    def updateResourcesByRol(self, pk, data):
        rol = self.rol_repository.get_by_id(pk)
        resources = self.resource_respository.filter_custom(rol=rol.pk,)
        current_resources_ids = set(resources.values_list('id', flat=True))
        payload_resources_ids = set(data)

        resources_to_add = payload_resources_ids - current_resources_ids
        resources_to_remove = current_resources_ids - resources_to_add

        print("Actuales", current_resources_ids)
        print("Nuevos", payload_resources_ids)
        print("Total", resources_to_add)
        print("Eliminar", resources_to_remove)
        
        for resource in resources_to_add:
            body = {"rol_id": rol.pk, "resource_id": resource}
            self.rol_resource_repository.create(body)
            
        for resource in resources_to_remove:
            x = self.rol_resource_repository.filter_custom(resource_id=resource).first()
            if x is not None:
                self.rol_resource_repository.delete(x.pk)

        return self.serializer({"OK": "OK"}).data

    def getPermissionsByRol(self):
        pass

    def updatePermissionByRol(self):
        pass

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
