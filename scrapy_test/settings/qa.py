"""Production settings and globals."""


from os import environ
import os

from postgresify import postgresify
import sys

from common import *


########## EMAIL CONFIGURATION
# See: Django Skel for more examples
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = postgresify()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: django skell for robust examples
########## END CACHE CONFIGURATION


########## LOGGING CONFIGURATION
# See: Raven sends errors to sentry
INSTALLED_APPS += (
  'raven.contrib.django.raven_compat',
)

LOGGING['handlers']['console_handler'] = {
  'level': 'INFO',
  'class': 'logging.StreamHandler',
  'formatter': 'standard',
  'stream': sys.stdout # http://stackoverflow.com/questions/11866322/heroku-logs-for-django-projects-missing-errors
}

LOGGING['handlers']['exception_handler'] = {
  'level': 'ERROR',
  'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
  }

app_logger = {
  'handlers': ['console_handler', 'exception_handler'],
  'level': 'INFO',
  'propagate': False
}

LOGGING['loggers'] = {
  '': {
    'handlers': ['console_handler'],
    'level': 'INFO',
    'propagate': True
  },
  'django.request': {
    'handlers': ['console_handler'],
    'level': 'WARNING',
    'propagate': False
  },
  'scrapy_test.aggregates': app_logger,
  'scrapy_test.apps': app_logger,
  'scrapy_test.libs': app_logger
}
########## END LOGGING CONFIGURATION

########## CELERY CONFIGURATION
# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-transport
BROKER_TRANSPORT = 'django'

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend
CELERY_RESULT_BACKEND = 'database'
########## END CELERY CONFIGURATION

########## STORAGE CONFIGURATION
# See: Django skell for robust examples
########## END STORAGE CONFIGURATION


########## COMPRESSION CONFIGURATION
# See: Django skell for robust examples
########## END COMPRESSION CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)
########## END SECRET CONFIGURATION

########## ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.herokuapp.com', '.nextlanding.com']
########## END ALLOWED HOST CONFIGURATION

########## CORS CONFIGURATION
CORS_ORIGIN_REGEX_WHITELIST = (
  '^http(s)?://qa.nextlanding\.com/?',
)
########## END CORS CONFIGURATION

########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES += (
  'sslify.middleware.SSLifyMiddleware',
  # ...
)

PROXY_URL = os.environ['PROXY_URL']
PROXY_USERNAME = os.environ['PROXY_USERNAME']
PROXY_PASSWORD = os.environ['PROXY_PASSWORD']
########## END MIDDLEWARE CONFIGURATION
