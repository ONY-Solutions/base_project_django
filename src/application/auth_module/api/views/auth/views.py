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
class AuthView(ViewSet):
    
    def get_serializer_class(self):
        return ResourceSerializer
    
    @property
    def get_service(self):
        return AuthModuleRepositoryFactory.get_security_service(self.get_serializer_class())
    
    @action(detail=False, methods=["POST"])
    def login(self, request):
        data = {}

        if 'email' in request.data:
            data["username"] = request.data.get("email",None)
            data["password"] = request.data.get("password",None)
        else:
            data = request.data

        validator = AuthValidator(data=data)

        if validator.is_valid():
            token = get_tokens_for_user(validator.validated_data)
        
            roles = [x.id for x in validator.validated_data.roles.all()]
            
            resources = self.get_service.getAllResourcesByRol(related={"resource_parent"},filter={"rol__in": roles})
            
            return Response({"user": {
                "first_name": validator.validated_data.first_name,
                "last_name": validator.validated_data.last_name,
                "email": validator.validated_data.email
                }, 
                "token":{**token}, 
                "resources": resources["data"]
                }, status=status.HTTP_200_OK)
        return Response({"Invalid credentias"}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=["POST"])
    def register(self, request):
        pass