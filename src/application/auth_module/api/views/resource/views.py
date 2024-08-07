# views.py

from rest_framework import viewsets, status
from rest_framework.response import Response

from config.core.constants.response_messages import ResponseMessages

from src.application.auth_module.api.repositories.factory_repository import (
    AuthModuleRepositoryFactory
)
from src.application.auth_module.api.serializers.resource_serializers import (
    ResourceSerializer
)
from src.application.auth_module.api.validators.resource_validators import (
    ResourceCreateValidator
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
        return Response(res)

    def retrieve(self, request, pk=None):
        res = self.get_service.get_by_id(pk)
        return Response(res)

    def create(self, request):
        ResourceCreateValidator().validate(data=request.data)
        try:
            self.get_service.create(request.data)
            return Response(ResponseMessages.CREATED, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(e.args, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        person = self.get_service.get_by_id(pk)
        if person is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ResourceSerializer(person, data=request.data)
        if serializer.is_valid():
            updated_person = self.get_service.update(pk, serializer.validated_data)
            return Response(ResourceSerializer(updated_person).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        person = self.get_service.get_by_id(pk)
        if person is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        self.get_service.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
