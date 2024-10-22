# views.py

from rest_framework import viewsets, status
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


class ResourceViewSet(viewsets.ViewSet):

    def get_serializer_class(self):
        return ResourceSerializer

    @property
    def get_service(self):
        return AuthModuleRepositoryFactory.get_resource_service(
            self.get_serializer_class()
        )

    def list(self, request):
        res = self.get_service.get_all()
        return Response(**res)

    def retrieve(self, request, pk=None):
        res = self.get_service.get_by_id(pk)
        return Response(**res)

    def create(self, request):
        ResourcesPayloadValidateSerializer().validate(request.data)
        data = request.data
        res = self.get_service.create(data)
        return Response(**res)

    def update(self, request, pk=None):
        data = request.data
        serializer = ResourceUpdateSerializer(data=data)

        if serializer.is_valid():
            res = self.get_service.update(pk, serializer.data)
            return Response(**res)
        return Response(serializer.errors, 404)

    def destroy(self, request, pk=None):
        res = self.get_service.delete(pk)
        return Response(**res)
