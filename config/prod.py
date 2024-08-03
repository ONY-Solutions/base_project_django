from config.base import *
from config.database import DATABASE_CONFIG

DEBUG = True

INSTALLED_APPS += []

ALLOWED_HOSTS = []

MIDDLEWARE += []

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASE = env("DATABASE")

DATABASES = {'default': DATABASE_CONFIG["prod"][DATABASE]}
