# views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from src.application.auth_module.api.repositories.factory_repository import (
    AuthModuleRepositoryFactory,
)
from src.application.auth_module.api.serializers.person_serializers import (
    PersonSerializer,
    PersonCreateSerializer,
)


class PersonViewSet(viewsets.ViewSet):

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PersonSerializer
        return PersonCreateSerializer

    @property
    def get_service(self):
        return AuthModuleRepositoryFactory.get_person_service(
            self.get_serializer_class()
        )

    def list(self, request):
        res = self.get_service.get_all()
        return Response(res)

    def retrieve(self, request, pk=None):
        res = self.get_service.get_by_id(pk)
        return Response(res)

    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            person = self.get_service.create(serializer.validated_data)
            return Response(
                PersonSerializer(person).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        person = self.get_service.get_by_id(pk)
        if person is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            updated_person = self.get_service.update(pk, serializer.validated_data)
            return Response(PersonSerializer(updated_person).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        person = self.get_service.get_by_id(pk)
        if person is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        self.get_service.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
