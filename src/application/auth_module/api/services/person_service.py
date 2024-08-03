from src.application.auth_module.api.repositories.factory_repository import AuthModuleRepositoryFactory
from src.application.auth_module.api.serializers.person_serializers import PersonSerializer

class PersonService:

    @property
    def get_repository(self):
        return AuthModuleRepositoryFactory.get_person_repository()
    
    def get_all(self):
        pass
    def get_by_id(self,pk):
        try:
            return  PersonSerializer(self.get_repository.get_by_id(pk)).data
        except Exception as e :
            return  e.args
        
    def create(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass