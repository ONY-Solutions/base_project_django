from src.interfaces.repository.base_repository import BaseRepository
from src.application.auth_module.models.rol import Rol_Resource

class RolResourceRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(Rol_Resource)
