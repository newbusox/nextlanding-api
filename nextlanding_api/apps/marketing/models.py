import logging

from django.db import models, transaction
from django_hstore import hstore
from nextlanding_api.apps.marketing.enums import ProductChoices, DidNotRespondChoices

logger = logging.getLogger(__name__)


class Correspondence(models.Model):
  objects = hstore.HStoreManager()

  to = models.TextField()
  from_address = models.TextField()

  from_first_name = models.CharField(max_length=255, blank=True, null=True)
  from_last_name = models.CharField(max_length=255, blank=True, null=True)

  product = models.PositiveSmallIntegerField(max_length=2, choices=ProductChoices)

  subject = models.TextField(blank=True, null=True)

  incoming_text = models.TextField(blank=True, null=True)
  incoming_html = models.TextField(blank=True, null=True)

  outgoing_text = models.TextField(blank=True, null=True)
  outgoing_html = models.TextField(blank=True, null=True)

  responded = models.BooleanField()
  did_not_respond_reason = models.PositiveSmallIntegerField(max_length=2, choices=DidNotRespondChoices, blank=True,
                                                      null=True)

  data = hstore.DictionaryField()

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        super(Correspondence, self).save(*args, **kwargs)
    else:
      from nextlanding_api.apps.marketing.services import correspondence_service
      correspondence_service.save_or_update(self)

  def __unicode__(self):
    return 'Correspondence #' + str(self.pk)

class MarketingEmailAccount(models.Model):
  email_addresses = models.TextField()
  product = models.PositiveSmallIntegerField(max_length=2, choices=ProductChoices)
  ignore_keywords = models.TextField(blank=True, null=True)

  def __unicode__(self):
    return 'MarketingEmailAccount #' + str(self.product)
