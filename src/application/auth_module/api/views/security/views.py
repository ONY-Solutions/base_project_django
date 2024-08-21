# views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from src.application.auth_module.api.repositories.factory_repository import (
    AuthModuleRepositoryFactory
)
from src.application.auth_module.api.serializers.security_serializers import (
    ResourcesByRolSerializer, PermissionByRolSerializer
)


class SecurityViewSet(viewsets.ViewSet):

    def get_serializer_class(self):
        if self.action in ["getResourcesByRol", "updateResourcesByRol"]:
            return ResourcesByRolSerializer
        return PermissionByRolSerializer

    @property
    def get_service(self):
        return AuthModuleRepositoryFactory.get_security_service(self.get_serializer_class())

    @action(detail=False, methods=["GET"], url_path="getResourcesByRol/(?P<pk>[^/.]+)")
    def getResourcesByRol(self, request, pk=None):
        res = self.get_service.getResourcesByRol(pk)
        return Response(**res)

    @action(detail=False, methods=["PUT"], url_path="updateResourcesByRol/(?P<pk>[^/.]+)")
    def updateResourcesByRol(self, request, pk=None):
        data = request.data["resources"]
        res = self.get_service.updateResourcesByRol(pk, data)
        return Response(**res)

    @action(detail=False, methods=["GET"], url_path="getPermissionByRol/(?P<pk>[^/.]+)")
    def getPermissionByRol(self, request, pk=None):
        res = self.get_service.getPermissionsByRol(pk)
        return Response(**res) 

    @action(detail=False, methods=["PUT"], url_path="updatePermissionByRol/(?P<pk>[^/.]+)")
    def updatePermissionByRol(self, request, pk=None):
        data = request.data["permissions"]
        res = self.get_service.updatePermissionByRol(pk, data)
        return Response(**res)