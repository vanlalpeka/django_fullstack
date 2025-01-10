# filepath: django_fullstack/main/test_settings.py
from .settings import *

# Override settings for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Other test-specific settings