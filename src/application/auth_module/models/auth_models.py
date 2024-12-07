from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from src.application.default.base_models import BaseModel
from src.application.auth_module.models.rol import Rol
from src.application.default.mixins import AuditModelMixin

class Master(BaseModel, AuditModelMixin):
    code = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    order = models.IntegerField(null=True, blank=True)
    note = models.CharField(max_length=250, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')


    class Meta:
        db_table = 'master'
        indexes = [
            models.Index(fields=['parent'], name='master_parent_id_idx'),
        ]


class Country(BaseModel):
    name = models.CharField(max_length=200)
    sap = models.CharField(max_length=10)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"


class Deparment(BaseModel):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "deparment"
        verbose_name_plural = "deparments"


class City(BaseModel):
    sap = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    deparment = models.ForeignKey(
        Deparment, on_delete=models.SET_NULL, blank=True, null=True
    )
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"


class Person(BaseModel):
    fullname = models.CharField(max_length=150, blank=False, default="")
    identification = models.CharField(
        max_length=40, unique=True, blank=False, default=""
    )
    email = models.EmailField(_("email address"), blank=False, default="")

    class Meta:
        verbose_name = "Persons"
        verbose_name_plural = "Persons"


class User(AbstractUser, BaseModel):
    username = models.CharField(blank=False, null=False, unique=True, max_length=256)
    password = models.CharField(max_length=100)
    person = models.ForeignKey(
        Person, on_delete=models.SET_NULL, blank=True, null=True, db_index=True
    )

    roles = models.ManyToManyField(Rol, related_name="user_roles", db_index=True)

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"
