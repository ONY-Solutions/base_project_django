# views.py

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from src.interfaces.utils.auth_utils import get_tokens_for_user
from src.application.auth_module.api.validators.auth_validator import AuthValidator
from src.application.auth_module.api.repositories.factory_repository import (
    AuthModuleRepositoryFactory,
)
from src.application.auth_module.api.serializers.resource_serializers import ResourceSerializer
from src.application.auth_module.api.serializers.auth_serializer import AuthSerializer, SchemaResponseLogin, SchemaResponseResources
from src.application.auth_module.api.serializers.user_serializers import UserSerializer
from drf_spectacular.utils import extend_schema
from src.application.auth_module.api.serializers.rol_serializer import RolValidateSerializer
from src.interfaces.helpers.error_handrer_catch import handle_view_errors
from src.application.default.view_default import BaseViewSet

class AuthView(BaseViewSet):
    factory = None

    def get_serializer_class(self):
        if self.action == "login":
            return AuthSerializer
        return ResourceSerializer
    
    @property
    def get_service(self):
        if not self.factory:
            self.factory = AuthModuleRepositoryFactory.get_security_service(self.get_serializer_class())
        return self.factory
    
    @extend_schema(
        responses={200: SchemaResponseLogin},
    )
    @action(detail=False, methods=["POST"])
    def login(self, request):

        validator = AuthValidator(data=request.data)

        if validator.is_valid():
            token = get_tokens_for_user(validator.validated_data)
            return Response({ "token" :{ **token } }, status=status.HTTP_200_OK)
        return Response({"Invalid credentias"}, status=status.HTTP_401_UNAUTHORIZED)

    @extend_schema(
        responses={200: SchemaResponseResources}
    )
    @action(detail=False, methods=["GET"])
    @handle_view_errors()
    def getResources(self, request):

        self.get_service.serializer = RolValidateSerializer
        roles = self.get_service.getAllRolesByUser(request.user.id)
        roles = [x["id"] for x in roles]

        resources = self.get_service.getAllResourcesByRol(related={"resource_parent"},filter={"rol__in": roles})
        user = UserSerializer([request.user], many=True)    
        
        return Response({"user": user.data[0], "resources": resources},status=status.HTTP_200_OK)

    @action(detail=False, methods=["POST"])
    def register(self, request):
        pass