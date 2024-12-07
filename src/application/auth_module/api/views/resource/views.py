# views.py

from rest_framework import status
from rest_framework.response import Response

from src.application.auth_module.api.repositories.factory_repository import (
    AuthModuleRepositoryFactory
)
from src.application.auth_module.api.serializers.resource_serializers import (
    ResourceSerializer
)
from src.application.auth_module.api.validators.resource_validators import (
    ResourcesPayloadValidateSerializer, ResourceUpdateSerializer
)
from drf_spectacular.utils import extend_schema
from src.interfaces.helpers.error_handrer_catch import handle_view_errors
from src.application.default.view_default import BaseViewSet

class ResourceViewSet(BaseViewSet):

    def get_serializer_class(self):
        return ResourceSerializer

    @property
    def get_service(self):
        return AuthModuleRepositoryFactory.get_resource_service(
            self.get_serializer_class()
        )

    def list(self, request):
        res = self.get_service.get_all()
        serializer = self.get_serializer_data(res, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @handle_view_errors()
    def retrieve(self, request, pk=None):
        res = self.get_service.get_by_id(pk)
        serializer = self.get_serializer_data(res).data
        return Response({**serializer}, status=status.HTTP_200_OK)
    
    @extend_schema(request=ResourcesPayloadValidateSerializer)
    @handle_view_errors()
    def create(self, request):
        ResourcesPayloadValidateSerializer().validate(request.data)
        data = request.data
        res = self.get_service.create(data)
        return Response(res, status=status.HTTP_200_OK)

    @extend_schema(request=ResourceUpdateSerializer)
    @handle_view_errors()
    def update(self, request, pk=None):
        data = request.data
        serializer = ResourceUpdateSerializer(data=data)

        if serializer.is_valid():
            res = self.get_service.update(pk, serializer.data)
            serializer = self.get_serializer_data(res).data
            return Response({**serializer}, status=status.HTTP_200_OK)
        return Response(serializer.errors, 404)

    @handle_view_errors()
    def destroy(self, request, pk=None):
        res = self.get_service.delete(pk)
        serializer = self.get_serializer_data(res).data
        return Response({**serializer}, status=status.HTTP_200_OK)
