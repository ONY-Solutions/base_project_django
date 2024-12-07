from django.db import models
from src.application.default.base_models import BaseModel
from src.application.default.mixins import AuditModelMixin

class Resource(BaseModel, AuditModelMixin):
    name = models.CharField(max_length=30, null=False)
    path = models.CharField(max_length=30, null=False, unique=True)
    icon = models.CharField(max_length=30, null=False, default="")
    resource_parent = models.ForeignKey(
        "Resource", null=True, blank=True, on_delete=models.SET_NULL
    )
    rol = models.ManyToManyField(
        "Rol", through="Rol_Resource", related_name="rol_resources"
    )
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "resource"
        verbose_name_plural = "resources"
