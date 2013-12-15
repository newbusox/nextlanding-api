from django.db import models, transaction
from jsonfield import JSONField


class PotentialSearch(models.Model):
  search_attrs = JSONField()

  purchased = models.BooleanField()

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  #do not use foreign keys for aggregates
  search_aggregate_id = models.IntegerField(blank=True, null=True)

  class Meta:
    app_label = 'domain'


  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        super(PotentialSearch, self).save(*args, **kwargs)
    else:
      from nextlanding_api.apps.domain.search.services import potential_search_service

      potential_search_service.save_or_update(self)

  def __unicode__(self):
    return 'PotentialSearch #' + str(self.pk)


class SearchEmailerSender(models.Model):
  #this represents the model to be used for sending emails for a search. The body, subject can be modified and saved.

  #do not use foreign keys for aggregates
  search_aggregate_id = models.IntegerField()

  specified_location = models.CharField(max_length=2048)
  description = models.TextField()

  from_name = models.CharField(max_length=2048, blank=True, null=True)
  subject = models.TextField()
  body = models.TextField()

  class Meta:
    app_label = 'domain'

  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        super(SearchEmailerSender, self).save(*args, **kwargs)
    else:
      from nextlanding_api.apps.domain.search.services import emailer_sender_service

      emailer_sender_service.save_or_update(self)

  def __unicode__(self):
    return 'SearchEmailerSender #' + str(self.pk)
