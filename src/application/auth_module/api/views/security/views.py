# views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from src.application.auth_module.api.repositories.factory_repository import (
    AuthModuleRepositoryFactory
)
from src.application.auth_module.api.serializers.resource_serializers import (
    ResourceSerializer
)
from src.application.auth_module.api.serializers.security_serializers import (
    ResourcesByRolSerializer
)


class SecurityViewSet(viewsets.ViewSet):

    def get_serializer_class(self):
        if self.action == "getResourcesByRol" or self.action == "updateResourcesByRol":
            return ResourcesByRolSerializer
        return ResourceSerializer

    @property
    def get_service(self):
        if self.action == "getResourcesByRol" or self.action == "updateResourcesByRol":
            return AuthModuleRepositoryFactory.get_rol_resource_service(self.get_serializer_class())
        return AuthModuleRepositoryFactory.get_resource_service(self.get_serializer_class())

    @action(detail=False, methods=["GET"], url_path="getResourcesByRol/(?P<pk>[^/.]+)")
    def getResourcesByRol(self, request, pk=None):
        res = self.get_service.getResourcesByRol(pk)
        return Response(res)

    @action(detail=False, methods=["PUT"], url_path="updateResourcesByRol/(?P<pk>[^/.]+)")
    def updateResourcesByRol(self, request, pk=None):
        data = request.data["resources"]
        res = self.get_service.updateResourcesByRol(pk, data)
        return Response(res)

    def getPermissionByRol(self, request, pk=None):
        pass

    def updatePermissionByRol(self, request, pk=None):
        pass
