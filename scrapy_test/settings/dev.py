"""Development settings and globals."""


from os.path import join, normpath

from common import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION

########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
#celery hijacks its logging to prevent other libs from screwing it up. In dev only, it'd be nice to write to a log file.
#http://docs.celeryproject.org/en/latest/configuration.html#logging
#why: http://stackoverflow.com/a/6942030/173957
CELERYD_HIJACK_ROOT_LOGGER = False

LOGGING['handlers']['console_handler'] = {
  'level': 'DEBUG',
  'class': 'logging.StreamHandler',
  'formatter': 'standard'
}

LOGGING['handlers']['file_handler'] = {
  'level': 'DEBUG',
  'class': 'logging.handlers.RotatingFileHandler',
  'filename': 'logs/app.log',
  'maxBytes': 1024 * 1024 * 5, # 5 MB
  'backupCount': 5,
  'formatter': 'standard',
  }

LOGGING['handlers']['request_handler'] = {
  'level': 'DEBUG',
  'class': 'logging.handlers.RotatingFileHandler',
  'filename': 'logs/django_request.log',
  'maxBytes': 1024 * 1024 * 5, # 5 MB
  'backupCount': 5,
  'formatter': 'standard',
  }

LOGGING['handlers']['exception_handler'] = {
  'level': 'ERROR',
  'class': 'logging.handlers.RotatingFileHandler',
  'filename': 'logs/error.log',
  'maxBytes': 1024 * 1024 * 5, # 5 MB
  'backupCount': 5,
  'formatter': 'standard',
  }

app_logger = {
  'handlers': ['console_handler', 'file_handler', 'exception_handler'],
  'level': 'DEBUG',
  'propagate': False
}

LOGGING['loggers'] = {
  '': {
    'handlers': ['console_handler', 'file_handler'],
    'level': 'DEBUG',
    'propagate': True
  },
  'django.request': {
    'handlers': ['request_handler', 'exception_handler'],
    'level': 'DEBUG',
    'propagate': False
  },
  'aggregates': app_logger,
  'apps': app_logger,
  'libs': app_logger,
  'celery.task': app_logger
}
########## END LOGGING CONFIGURATION

########## CELERY CONFIGURATION
# See: http://docs.celeryq.org/en/latest/configuration.html#celery-always-eager
CELERY_ALWAYS_EAGER = True

CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

BROKER_TRANSPORT = 'django'

CELERY_RESULT_BACKEND = 'database'
########## END CELERY CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
)
########## END TOOLBAR CONFIGURATION


########## TESTING CONFIGURATION
########## END TESTING CONFIGURATION


########## CORS CONFIGURATION
CORS_ORIGIN_REGEX_WHITELIST = (
  '^http://localhost:\d{1,4}/?',
)
########## END CORS CONFIGURATION

########## DJANGO EXTENSIONS CONFIGURATION
INSTALLED_APPS += (
  'django_extensions',
)
########## END DJANGO EXTENSIONS CONFIGURATION
