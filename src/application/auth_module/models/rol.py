from django.db import models
from src.application.default.base_models import BaseModel
from src.application.auth_module.models.resource import Resource
from src.application.auth_module.models.permissions import Permission


class Rol(BaseModel):
    name = models.CharField(max_length=30, null=False, unique=True)
    resources = models.ManyToManyField(
        Resource, through="Rol_Resource", related_name="rol_resources"
    )
    permissions = models.ManyToManyField(
        Permission, through="Rol_Permission", related_name="rol_permissions"
    )

    class Meta:
        verbose_name = "rol"
        verbose_name_plural = "roles"


class Rol_Resource(BaseModel):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


class Rol_Permission(BaseModel):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
