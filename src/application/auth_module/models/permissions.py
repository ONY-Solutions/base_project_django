from django.db import models
from src.application.default.base_models import BaseModel
from src.application.default.mixins import AuditModelMixin

class Permission(BaseModel, AuditModelMixin):
    name = models.CharField(max_length=30, null=False)
    path = models.CharField(max_length=30, null=False, unique=True)
    method = models.CharField(max_length=30, null=False)
    rol = models.ManyToManyField(
        "Rol", through="Rol_Permission", related_name="rol_permissions"
    )
        

    class Meta:
        verbose_name = "permission"
        verbose_name_plural = "permissions"
