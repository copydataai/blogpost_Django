"""Development settings."""
from .base import *
from .base import env

DEBUG = True

# Security
SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
]

INSTALLED_APPS += ['django_extensions']
