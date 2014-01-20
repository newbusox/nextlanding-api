"""Production settings and globals."""


from os import environ
import os

from postgresify import postgresify
import sys
import urlparse

from common import *


########## EMAIL CONFIGURATION
# See: Django Skel for more examples
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = postgresify()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
redis_url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
CACHES = {
  'default': {
    'BACKEND': 'redis_cache.RedisCache',
    'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
    'OPTIONS': {
      'PASSWORD': redis_url.password,
      'DB': 0,
      }
  }
}
########## END CACHE CONFIGURATION


########## LOGGING CONFIGURATION
# See: Raven sends errors to sentry
INSTALLED_APPS += (
  'raven.contrib.django.raven_compat',
)

CELERYD_HIJACK_ROOT_LOGGER = False
CELERY_REDIRECT_STDOUTS = False

APP_LOG_LEVEL = os.environ.get('APP_LOG_LEVEL','INFO')
SCRAPY_LOG_LEVEL = os.environ.get('SCRAPY_LOG_LEVEL','ERROR')

LOGGING['handlers']['console_handler'] = {
  'level': APP_LOG_LEVEL,
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
  'level': APP_LOG_LEVEL,
  'propagate': False
}

LOGGING['loggers'] = {
  '': {
    'handlers': ['console_handler'],
    'level': 'WARNING',
    'propagate': True
  },
  'django.request': {
    'handlers': ['console_handler'],
    'level': 'WARNING',
    'propagate': False
  },
  'django.db.backends': {
    'level': APP_LOG_LEVEL,
  },
  'nextlanding_api.aggregates': app_logger,
  'nextlanding_api.apps': app_logger,
  'nextlanding_api.libs': app_logger,
  'celery': app_logger,
}
########## END LOGGING CONFIGURATION

########## CELERY CONFIGURATION
# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-transport
celery_redis_url = os.environ.get('REDISCLOUD_URL')
BROKER_URL = celery_redis_url

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

# See: http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#caveats
# You have to set a transport option to prefix the messages so that they will only be received by the active virtual host:

# If a task is not acknowledged within the Visibility Timeout the task will be redelivered to another worker and executed.
# This causes problems with ETA/countdown/retry tasks where the time to execute exceeds the visibility timeout; in
# fact if that happens it will be executed again, and again in a loop.
# 3600 (1 hour) * 48 hours
BROKER_TRANSPORT_OPTIONS = {'fanout_prefix': True, 'visibility_timeout': CELERY_LONGEST_RUNNING_TASK_SECONDS}

# BROKER_POOL_LIMIT Is not set
# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-redis-max-connections
# http://docs.celeryproject.org/en/latest/configuration.html#broker-pool-limit
# http://stackoverflow.com/questions/16391428/heroku-celery-exceeding-connection-limit
# http://stackoverflow.com/questions/12013220/celery-creating-a-new-connection-for-each-task
# Our Redis plan only supports 10 connections and some are used on the front end.
# The front end will have 4 gunicorn workers
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
ALLOWED_HOSTS = ['.herokuapp.com', 'api.nextlanding.com']
########## END ALLOWED HOST CONFIGURATION

########## CORS CONFIGURATION
CORS_ORIGIN_REGEX_WHITELIST = (
  '^http(s)?://www.nextlanding\.com/?',
)
########## END CORS CONFIGURATION

########## MIDDLEWARE CONFIGURATION
PROXY_URL = os.environ['PROXY_URL']
PROXY_USERNAME = os.environ['PROXY_USERNAME']
PROXY_PASSWORD = os.environ['PROXY_PASSWORD']
########## END MIDDLEWARE CONFIGURATION

########## ANALYTICS CONFIGURATION
MIXPANEL_API_TOKEN = os.environ['MIXPANEL_API_TOKEN']
########## END ANALYTICS CONFIGURATION
