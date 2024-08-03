# urls.py

from django.urls import path, include

urlpatterns = [
    path('', include('src.application.auth_module.api.views.person.urls'), name='person'),
    path('user', include('src.application.auth_module.api.views.user.urls'), name='user'),
]