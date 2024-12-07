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
from drf_spectacular.utils import extend_schema
from src.interfaces.helpers.error_handrer_catch import handle_view_errors

class SecurityViewSet(viewsets.ViewSet):

    def get_serializer_class(self):
        if self.action in ["getResourcesByRol", "updateResourcesByRol"]:
            return ResourcesByRolSerializer
        elif self.action in ["assingUserRol"]:
            return UserSerializer
        return PermissionByRolSerializer

    def get_serializer_data(self, data_to_serializar):
        serializer = self.get_serializer_class()
        return serializer(data_to_serializar)

    @property
    def get_service(self):
        return AuthModuleRepositoryFactory.get_security_service()
    
    @action(detail=False, methods=["POST"], url_path="assingUserRol/(?P<pk>[^/.]+)")
    @handle_view_errors()
    def assingUserRol(self, request,pk=None):
        validator = UserRolValidator(data=request.data)

        if validator.is_valid():
            service_response = self.get_service.asingUserRol(pk,validator.data["roles"])
            serializer = self.get_serializer_data(service_response).data
            return Response({**serializer}, status=status.HTTP_200_OK)

        return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["GET"], url_path="getResourcesByRol/(?P<pk>[^/.]+)")
    @handle_view_errors()
    def getResourcesByRol(self, request, pk=None):        
        service_response = self.get_service.getResourcesByRol(pk)
        serializer = self.get_serializer_data(service_response).data
        return Response({**serializer}, status=status.HTTP_200_OK)
        

    @extend_schema(request=RolResourceValidate)
    @action(detail=False, methods=["PUT"], url_path="updateResourcesByRol/(?P<pk>[^/.]+)")
    @handle_view_errors()
    def updateResourcesByRol(self, request, pk=None):
        validate = RolResourceValidate(data=request.data)

        if validate.is_valid():
            service_response = self.get_service.updateResourcesByRol(pk, validate.data["resources"])
            serializer = self.get_serializer_data(service_response).data
            return Response({**serializer}, status=status.HTTP_200_OK)

        return Response(validate.errors,status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["GET"], url_path="getPermissionByRol/(?P<pk>[^/.]+)")
    @handle_view_errors()
    def getPermissionByRol(self, request, pk=None):
        service_response = self.get_service.getPermissionsByRol(pk)
        serializer = self.get_serializer_data(service_response).data
        return Response({**serializer}, status=status.HTTP_200_OK)

    @extend_schema(request=RolPermissionsValidate)
    @action(detail=False, methods=["PUT"], url_path="updatePermissionByRol/(?P<pk>[^/.]+)")
    @handle_view_errors()
    def updatePermissionByRol(self, request, pk=None):

        validate = RolPermissionsValidate(data=request.data)
        if validate.is_valid():

            service_response = self.get_service.updatePermissionByRol(pk, validate.data["permissions"])
            serializer = self.get_serializer_data(service_response).data
            return Response({**serializer}, status=status.HTTP_200_OK)

        return Response(validate.errors,status=status.HTTP_400_BAD_REQUEST)
