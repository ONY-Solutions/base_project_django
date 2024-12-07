from rest_framework import status
from src.application.auth_module.api.serializers.permission_serializer import PermissionValidateSerializer, PermissionUpdateValidateSerializer, PermissionCreateValidateSerializer
from src.application.auth_module.api.repositories.factory_repository import (
    AuthModuleRepositoryFactory,
)
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from src.interfaces.helpers.error_handrer_catch import handle_view_errors
from src.application.default.view_default import BaseViewSet

class PermissionView(BaseViewSet):

    def get_serializer_class(self):
        return PermissionCreateValidateSerializer

    @property
    def get_service(self):
        return AuthModuleRepositoryFactory.get_permission_service()

    def list(self, request):
        res = self.get_service.get_all()
        serializer = self.get_serializer_data(res, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @handle_view_errors()
    def retrieve(self, request, pk=None):
        
        """_summary_

        Returns:
            _type_: _description_
        """
        
        res = self.get_service.get_by_id(pk)
        serializer = self.get_serializer_data(res).data
        return Response({**serializer}, status=status.HTTP_200_OK)

    @handle_view_errors()
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = PermissionValidateSerializer(data=data)

        if serializer.is_valid():
            res = self.get_service.create(serializer.data)
            serializer = self.get_serializer_data(res).data
            return Response({**serializer}, status=status.HTTP_200_OK)
        return Response(serializer.errors, 404)

    @extend_schema(request=PermissionUpdateValidateSerializer)
    @handle_view_errors()
    def update(self, request, pk=None):

        data = request.data
        serializer = PermissionUpdateValidateSerializer(data=data)

        if serializer.is_valid():
            res = self.get_service.update(pk, serializer.data)
            serializer = self.get_serializer_data(res).data
            return Response({**serializer}, status=status.HTTP_200_OK)

        return Response(serializer.errors, 404)

    def destroy(self, request, pk=None):
        res = self.get_service.delete(pk)
        serializer = self.get_serializer_data(res).data
        return Response({**serializer}, status=status.HTTP_200_OK)
