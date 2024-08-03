from config.app.base import *
from config.db.database import DATABASE_CONFIG

DEBUG = True

COMMON_APPS = ['rest_framework']
THIRDS_APPS = ['src.application.auth_module']

INSTALLED_APPS = BASE_APPS + COMMON_APPS + THIRDS_APPS

ALLOWED_HOSTS = []

MIDDLEWARE += []

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASE = env("DATABASE")

DATABASES = {'default': DATABASE_CONFIG["prod"][DATABASE]}
