from src.interfaces.repository.base_repository import BaseRepository
from src.application.auth_module.models import Permission


class PermissionRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(Permission)

    def filter_by_rol(self, pk):
        return self.Model.objects.filter(rol=pk)
