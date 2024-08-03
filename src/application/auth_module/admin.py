from django.contrib import admin
from src.application.auth_module.models import (
    City,
    Country,
    Rol,
    Rol_Permission,
    Rol_Resource,
    Resource,
    Permission,
    Person,
    User,
    Deparment
)

# Register your models here.

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Rol)
admin.site.register(Rol_Permission)
admin.site.register(Rol_Resource)
admin.site.register(Resource)
admin.site.register(Permission)
admin.site.register(Person)
admin.site.register(User)
admin.site.register(Deparment)