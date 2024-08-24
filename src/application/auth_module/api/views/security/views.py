# views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from src.application.auth_module.api.repositories.factory_repository import (
    AuthModuleRepositoryFactory
)
from src.application.auth_module.api.serializers.security_serializers import (
    ResourcesByRolSerializer, PermissionByRolSerializer, 
)
from src.application.auth_module.api.validators.security_validators import RolResourceValidate, RolPermissionsValidate, UserRolValidator
from src.application.auth_module.api.serializers.user_serializers import UserSerializer
class SecurityViewSet(viewsets.ViewSet):

    def get_serializer_class(self):
        if self.action in ["getResourcesByRol", "updateResourcesByRol"]:
            return ResourcesByRolSerializer
        elif self.action in ["assingUserRol"]:
            return UserSerializer
        return PermissionByRolSerializer

    @property
    def get_service(self):
        return AuthModuleRepositoryFactory.get_security_service(self.get_serializer_class())
    
    @action(detail=False, methods=["POST"], url_path="assingUserRol/(?P<pk>[^/.]+)")
    def assingUserRol(self, request,pk=None):
        validator = UserRolValidator(data=request.data)

        if validator.is_valid():
            res = self.get_service.asingUserRol(pk,validator.data["roles"])
            return Response(**res)

        return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["GET"], url_path="getResourcesByRol/(?P<pk>[^/.]+)")
    def getResourcesByRol(self, request, pk=None):
        res = self.get_service.getResourcesByRol(pk)
        return Response(**res)

    @action(detail=False, methods=["PUT"], url_path="updateResourcesByRol/(?P<pk>[^/.]+)")
    def updateResourcesByRol(self, request, pk=None):
        validate = RolResourceValidate(data=request.data)

        if validate.is_valid():
            res = self.get_service.updateResourcesByRol(pk, validate.data["resources"])
            return Response(**res)

        return Response(validate.errors,status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["GET"], url_path="getPermissionByRol/(?P<pk>[^/.]+)")
    def getPermissionByRol(self, request, pk=None):
        res = self.get_service.getPermissionsByRol(pk)
        return Response(**res) 

    @action(detail=False, methods=["PUT"], url_path="updatePermissionByRol/(?P<pk>[^/.]+)")
    def updatePermissionByRol(self, request, pk=None):

        validate = RolPermissionsValidate(data=request.data)
        if validate.is_valid():

            res = self.get_service.updatePermissionByRol(pk, validate.data["permissions"])
            return Response(**res)

        return Response(validate.errors,status=status.HTTP_400_BAD_REQUEST)
