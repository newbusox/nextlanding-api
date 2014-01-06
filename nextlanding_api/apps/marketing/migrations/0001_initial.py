# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Correspondence'
        db.create_table(u'marketing_correspondence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('to', self.gf('django.db.models.fields.TextField')()),
            ('from_address', self.gf('django.db.models.fields.TextField')()),
            ('from_first_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('from_last_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('product', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2)),
            ('subject', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('incoming_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('incoming_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('outgoing_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('outgoing_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('responded', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('did_not_respond_reason', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2, null=True, blank=True)),
            ('data', self.gf('django_hstore.fields.DictionaryField')()),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'marketing', ['Correspondence'])

        # Adding model 'MarketingEmailAccount'
        db.create_table(u'marketing_marketingemailaccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_addresses', self.gf('django.db.models.fields.TextField')()),
            ('product', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2)),
            ('ignore_keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'marketing', ['MarketingEmailAccount'])


    def backwards(self, orm):
        # Deleting model 'Correspondence'
        db.delete_table(u'marketing_correspondence')

        # Deleting model 'MarketingEmailAccount'
        db.delete_table(u'marketing_marketingemailaccount')


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