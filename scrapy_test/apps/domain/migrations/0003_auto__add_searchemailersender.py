# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SearchEmailerSender'
        db.create_table(u'domain_searchemailersender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search_aggregate_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('specified_location', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('subject', self.gf('django.db.models.fields.TextField')()),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('domain', ['SearchEmailerSender'])


    def backwards(self, orm):
        # Deleting model 'SearchEmailerSender'
        db.delete_table(u'domain_searchemailersender')


    models = {
        'domain.potentialsearch': {
            'Meta': {'object_name': 'PotentialSearch'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchased': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_aggregate_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'search_attrs': ('jsonfield.fields.JSONField', [], {})
        },
        'domain.searchemailersender': {
            'Meta': {'object_name': 'SearchEmailerSender'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'search_aggregate_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'specified_location': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'subject': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['domain']