# urls.py

from django.urls import path, include

urlpatterns = [
    path('', include('src.application.auth_module.api.views.person.urls'), name='person'),
    path('', include('src.application.auth_module.api.views.resource.urls'), name='resource'),
    path('user', include('src.application.auth_module.api.views.user.urls'), name='user'),
    path('', include('src.application.auth_module.api.views.rol.urls'), name='rol'),
    path('', include(
        'src.application.auth_module.api.views.permission.urls'), name='permission'),
    path('', include('src.application.auth_module.api.views.rol_permission.urls'),
         name='rol-permission'),
]
