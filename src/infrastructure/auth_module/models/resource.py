from django.db import models
from src.application.default.base_models import BaseModel


class Resource(BaseModel):
    name = models.CharField(max_length=30, null=False)
    path = models.CharField(max_length=30, null=False, unique=True)
    resource_parent = models.ForeignKey(
        "Resource", null=True, blank=True, on_delete=models.SET_NULL
    )
    rol = models.ManyToManyField(
        "Rol", through="Rol_Resource", related_name="rol_resources"
    )

    class Meta:
        verbose_name = "resource"
        verbose_name_plural = "resources"
