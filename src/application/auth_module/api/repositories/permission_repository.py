from src.interfaces.repository.base_repository import BaseRepository
from src.application.auth_module.models.permissions import Permission


class PermissionRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(Permission)
