from src.interfaces.repository.base_repository import BaseRepository
from src.application.auth_module.models.resource import Resource

class ResourceRepository (BaseRepository):
    
    def __init__(self) -> None:
        super().__init__(Resource)