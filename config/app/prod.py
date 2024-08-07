from config.app.base import *
from config.db.database import DATABASE_CONFIG

DEBUG = True


THIRDS_APPS += []

INSTALLED_APPS = COMMON_APPS + THIRDS_APPS + MY_APPS 

ALLOWED_HOSTS = []

MIDDLEWARE += []

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASE = env("DATABASE")

DATABASES = {'default': DATABASE_CONFIG["prod"][DATABASE]}
