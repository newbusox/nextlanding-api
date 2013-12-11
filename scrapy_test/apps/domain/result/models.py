from django.db import models, transaction
from jsonfield import JSONField
from localflavor.us.models import PhoneNumberField


class SearchResult(models.Model):
  #do not use foreign keys for aggregates
  result_aggregate_id = models.IntegerField(unique=True)
  apartment_aggregate_id = models.IntegerField()
  search_aggregate_id = models.IntegerField()

  #can this apt be searched and used to be added to a search?
  is_available = models.BooleanField()

  address = models.CharField(max_length=255, blank=True, null=True)
  lat = models.FloatField()
  lng = models.FloatField()
  broker_fee = models.BooleanField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  bedroom_count = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bathroom_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  sqfeet = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

  listing_urls = JSONField(default=[])

  #these are listing-specific things
  last_updated_date = models.DateTimeField()
  description = models.TextField()
  contact_name = models.CharField(max_length=255, blank=True, null=True)
  contact_phone_number = PhoneNumberField(blank=True, null=True)
  contact_email_address = models.EmailField(blank=True, null=True)

  amenities = JSONField(blank=True, null=True)

  compliance_score = models.PositiveSmallIntegerField()
  availability_contact_response = models.TextField(blank=True, null=True)
  availability_last_response_date = models.DateTimeField(blank=True, null=True)
  availability_system_name = models.CharField(max_length=128) #availabile, different_user_notified_unavailable


  class Meta:
    app_label = 'domain'
    unique_together = ("apartment_aggregate_id", "search_aggregate_id")

  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        super(SearchResult, self).save(*args, **kwargs)
    else:
      from scrapy_test.apps.domain.result.services import search_result_service

      search_result_service.save_or_update(self)

  def __unicode__(self):
    return 'Search Result#' + str(self.pk)
