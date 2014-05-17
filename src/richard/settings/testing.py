# Override settings for test environment here

from .base import *
import os

# site_root is the parent directory
SITE_ROOT = os.path.dirname(os.path.dirname(__file__))

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(SITE_ROOT, '_test_whoosh_index'),
    },
}

DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

API = True

SECRET_KEY = 'richard-test'
LOGGING['loggers']['south'] = {'handlers': ['null_handler'],
                               'level': 'DEBUG',
                               'propagate': False}
