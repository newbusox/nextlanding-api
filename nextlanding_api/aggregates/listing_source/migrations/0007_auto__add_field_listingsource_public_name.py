# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ListingSource.public_name'
        db.add_column(u'listing_source_listingsource', 'public_name',
                      self.gf('django.db.models.fields.CharField')(default='Default', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ListingSource.public_name'
        db.delete_column(u'listing_source_listingsource', 'public_name')


    models = {
        u'listing_source.listingsource': {
            'Meta': {'object_name': 'ListingSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'public_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'trusted_geo_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['listing_source']