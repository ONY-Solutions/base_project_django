from src.interfaces.repository.base_repository import BaseRepository
from src.application.auth_module.models import Rol_Permission


class RolPermissionRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(Rol_Permission)
