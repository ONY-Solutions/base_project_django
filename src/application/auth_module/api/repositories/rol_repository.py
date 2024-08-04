from src.interfaces.repository.base_repository import BaseRepository
from src.application.auth_module.models.auth_models import Rol

class RolRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(Rol)
