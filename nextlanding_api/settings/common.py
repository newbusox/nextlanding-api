"""Common settings and globals."""


from datetime import timedelta
from os import environ
from os.path import abspath, basename, dirname, join, normpath
from sys import path

from djcelery import setup_loader


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
SYSTEM_EMAIL = ('System', 'system@nextlanding.com')
PUBLIC_EMAIL = ('Nextlanding', 'info@nextlanding.com')
ADMIN_EMAIL = ('Admin', 'admin@nextlanding.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ADMIN_EMAIL,
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = []

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = r"to(rkb!6lj3bwbz&qs2go0@)1ctjcx43lm6lerci#s_vpg*%mr"
########## END SECRET CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(DJANGO_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Use GZip compression to reduce bandwidth.
    'django.middleware.gzip.GZipMiddleware',

    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    'south',

    # Static file management:

    # Asynchronous task queue:
    'djcelery',
    'dynamic_scraper',
    'kombu.transport.django',

    # Database
    'reversion',

    # Mixpanel
    'mixpanel',

    # Rest API
    'rest_framework',

    #Headers
    'corsheaders',
)

LOCAL_APPS = (
  # AGGREGATES
  'nextlanding_api.aggregates.amenity',
  'nextlanding_api.aggregates.apartment',
  'nextlanding_api.aggregates.availability',
  'nextlanding_api.aggregates.listing',
  'nextlanding_api.aggregates.listing_source',
  'nextlanding_api.aggregates.result',
  'nextlanding_api.aggregates.search',
  # APPS
  'nextlanding_api.apps.communication_associater',
  'nextlanding_api.apps.domain',
  'nextlanding_api.apps.web_scraper',
  # LIBS
  'nextlanding_api.libs.common_domain',
  'nextlanding_api.libs.communication_utils',
  'nextlanding_api.libs.django_utils',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'formatters': {
    'standard': {
      'format': '[%(levelname)s] %(name)s: %(message)s'
    },
    },
  'handlers': {}
}
########## END LOGGING CONFIGURATION


########## CELERY CONFIGURATION
# See: http://celery.readthedocs.org/en/latest/configuration.html#celery-task-result-expires
CELERY_TASK_RESULT_EXPIRES = timedelta(minutes=30)

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# See: http://docs.celeryproject.org/en/master/configuration.html#std:setting-CELERY_CHORD_PROPAGATES
CELERY_CHORD_PROPAGATES = True

CELERY_IMPORTS = (
  'nextlanding_api.aggregates.apartment.services.apartment_tasks',
  'nextlanding_api.aggregates.listing.services.listing_tasks',
  'nextlanding_api.aggregates.result.services.result_tasks',
  'nextlanding_api.aggregates.search.services.search_tasks',
  'nextlanding_api.apps.communication_associater.availability.email.services.email_tasks',
  'nextlanding_api.apps.domain.search.services.potential_search_tasks',
  'nextlanding_api.apps.domain.search.services.emailer_sender_tasks',
  'nextlanding_api.apps.domain.apartment.services.add_apartment_to_search_tasks',
  'nextlanding_api.apps.domain.result.services.search_result_tasks',
  'nextlanding_api.apps.web_scraper.services.web_scraper_tasks',
  'nextlanding_api.libs.communication_utils.services.email_tasks',
)

# See: http://celery.github.com/celery/django/
setup_loader()
########## END CELERY CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
########## END WSGI CONFIGURATION


########## COMPRESSION CONFIGURATION
# See django skel for more info
########## END COMPRESSION CONFIGURATION

# ########## API CONFIGURATION
EXTERNAL_API_TOKEN = environ.get('EXTERNAL_API_TOKEN')
########## END API CONFIGURATION

########### EMAIL CONFIGURATION
SPAM_SCORE_THRESHOLD = environ.get('SPAM_SCORE_THRESHOLD', 2.3)
AVAILABILITY_FROM_EMAIL_ADDRESS_DOMAIN = environ.get('AVAILABILITY_FROM_EMAIL_ADDRESS_DOMAIN')
SENDGRID_USERNAME = environ.get('SENDGRID_USERNAME')
SENDGRID_PASSWORD = environ.get('SENDGRID_PASSWORD')
GMAIL_USERNAME = environ.get('GMAIL_USERNAME')
GMAIL_PASSWORD = environ.get('GMAIL_PASSWORD')
SECONDARY_EMAIL_DOMAINS = ('hous.craigslist.org',)
# these domains, like CL, will not work if you attach the result id to the "from" address because we cannot
# reliably use a service like sendgrid to send emails - we instead might need individual email addresses
BODY_RESULT_IDENTIFIER_DOMAINS = ('hous.craigslist.org','reply.craigslist.org')
########## END EMAIL CONFIGURATION

########### REST CONFIGURATION
REST_FRAMEWORK = {
  # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
  'PAGINATE_BY': 10
}
########## END REST CONFIGURATION

########## CORS CONFIGURATION
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_CREDENTIALS = True
########## END CORS CONFIGURATION

########### PAYMENT CONFIGURATION
STRIPE_SECRET_KEY = environ.get('STRIPE_SECRET_KEY')
SEARCH_PRICE = 35.00
########## END PAYMENT CONFIGURATION
