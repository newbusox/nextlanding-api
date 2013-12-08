from django.contrib import admin
from django.conf.urls import patterns, include, url
from scrapy_test.apps.rest_api import urls as api_urls

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# region Admin Urls
# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns(
  '',
  # Admin panel and documentation:
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', include(admin.site.urls)),
)
# endregion

# region Lib Urls

# endregion

# region App Urls
urlpatterns += patterns(
  '',
  url(r'^api/', include(api_urls)),
)
# endregion
