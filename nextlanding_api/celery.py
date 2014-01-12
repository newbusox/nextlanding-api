from __future__ import absolute_import
import os

from scrapy.utils.project import get_project_settings
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nextlanding_api.settings.dev')
os.environ.setdefault("SCRAPY_SETTINGS_MODULE", "nextlanding_api.apps.web_scraper.settings")

app = Celery('nextlanding_api')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# this will pre-warm scrapy and DDS. If we don't pre-cache this now, there will be a circular dependency between
# web_scraper_service -> ProcessBasedUtils.
get_project_settings()
