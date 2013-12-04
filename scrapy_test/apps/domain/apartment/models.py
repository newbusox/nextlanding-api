from django.db import models, transaction


class AddApartmentToSearch(models.Model):
  #this represents the model to be used for adding apts to a search

  #do not use foreign keys for aggregates
  apartment_aggregate_id = models.IntegerField(blank=True, null=True)

  class Meta:
    app_label = 'domain'

  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        super(AddApartmentToSearch, self).save(*args, **kwargs)
    else:
      from scrapy_test.apps.domain.apartment.services import add_apartment_to_search_service

      add_apartment_to_search_service.save_or_update(self)

  def __unicode__(self):
    return 'AddApartmentToSearch #' + str(self.pk)
