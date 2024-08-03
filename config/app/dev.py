from config.app.base import *
from config.db.database import DATABASE_CONFIG

DEBUG = True

ALLOWED_HOSTS = []

COMMON_APPS = ['rest_framework']
THIRDS_APPS = ['src.application.auth_module']

INSTALLED_APPS = BASE_APPS + COMMON_APPS + THIRDS_APPS

MIDDLEWARE += []

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASE = env.str("DATABASE", "sqlite")

DATABASES = {'default': DATABASE_CONFIG["local"][DATABASE]}
