from config.base import *
from config.database import DATABASE_CONFIG

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += []

MIDDLEWARE += []

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASE = env.str("DATABASE","sqlite")

DATABASES = {'default': DATABASE_CONFIG["local"][DATABASE]}
