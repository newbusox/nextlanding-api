# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        orm.ListingSource.objects.filter(pk=3).update(url="http://streeteasy.com/nyc/rentals/nyc/rental_type:frbo,brokernofee,brokerfee?sort_by=listed_desc")

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'listing_source.listingsource': {
            'Meta': {'object_name': 'ListingSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'trusted_geo_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['listing_source']
    symmetrical = True
