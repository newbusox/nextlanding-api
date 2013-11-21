# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Result'
        db.create_table(u'result_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='results', to=orm['apartment.Apartment'])),
            ('search', self.gf('django.db.models.fields.related.ForeignKey')(related_name='results', to=orm['search.Search'])),
            ('compliance_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2)),
            ('availability_contact_response', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('availability_last_response_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('availability_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='result_instance', to=orm['availability.Availability'])),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'result', ['Result'])

        # Adding unique constraint on 'Result', fields ['apartment', 'search']
        db.create_unique(u'result_result', ['apartment_id', 'search_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Result', fields ['apartment', 'search']
        db.delete_unique(u'result_result', ['apartment_id', 'search_id'])

        # Deleting model 'Result'
        db.delete_table(u'result_result')


    models = {
        u'apartment.apartment': {
            'Meta': {'unique_together': "(('lat', 'lng', 'price'),)", 'object_name': 'Apartment'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bathroom_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bedroom_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'broker_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'formatted_address': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'sqfeet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'availability.availability': {
            'Meta': {'object_name': 'Availability'},
            'aliases': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'system_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'result.result': {
            'Meta': {'unique_together': "(('apartment', 'search'),)", 'object_name': 'Result'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': u"orm['apartment.Apartment']"}),
            'availability_contact_response': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'availability_last_response_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'availability_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'result_instance'", 'to': u"orm['availability.Availability']"}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'compliance_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'search': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': u"orm['search.Search']"})
        },
        u'search.search': {
            'Meta': {'object_name': 'Search'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bathroom_max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bathroom_min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bedroom_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'bedroom_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'formatted_address': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'geo_boundary_points': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'no_fee_preferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price_max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'price_min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'specified_location': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'sqfeet_max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'sqfeet_min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['result']