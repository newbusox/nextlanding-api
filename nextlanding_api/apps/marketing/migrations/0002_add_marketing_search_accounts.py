# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from nextlanding_api.libs.django_utils.extensions.migrations import load_data


class Migration(DataMigration):

    def forwards(self, orm):
        load_data(orm, "0002_add_marketing_search_accounts.json")

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'marketing.correspondence': {
            'Meta': {'object_name': 'Correspondence'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django_hstore.fields.DictionaryField', [], {}),
            'did_not_respond_reason': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.TextField', [], {}),
            'from_first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'from_last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incoming_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'incoming_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'outgoing_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'outgoing_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2'}),
            'responded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'to': ('django.db.models.fields.TextField', [], {})
        },
        u'marketing.marketingemailaccount': {
            'Meta': {'object_name': 'MarketingEmailAccount'},
            'email_addresses': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignore_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['marketing']
    symmetrical = True
