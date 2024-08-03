from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from src.application.default.base_models import BaseModel

        
class Pais(BaseModel):
    name = models.CharField(max_length=200)
    sap = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

class Departamento(BaseModel):
    name = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, blank=True, null=True )

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        
class Ciudad(BaseModel):
    sap = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True )
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, blank=True, null=True )

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"


class Persons(BaseModel):
    fullname = models.CharField(max_length=150, blank=False, default="")
    identification = models.CharField(max_length=40, unique=True, blank=False, default="")
    email = models.EmailField(_("email address"), blank=False, default="")

    class Meta:
        verbose_name = "Persons"
        verbose_name_plural = "Persons"

class User(AbstractUser, BaseModel):
    username = models.CharField(blank=False, null=False, unique=True, max_length=256)
    password = models.CharField(max_length=100)
    person = models.ForeignKey(Persons, on_delete=models.SET_NULL, blank=True, null=True, db_index=True)
    
    roles = models.ManyToManyField(Group, related_name="user_roles", db_index=True)

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"
