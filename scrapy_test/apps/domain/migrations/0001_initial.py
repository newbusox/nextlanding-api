# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PotentialSearch'
        db.create_table(u'domain_potentialsearch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search_attrs', self.gf('jsonfield.fields.JSONField')()),
            ('purchased', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('search_aggregate_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('domain', ['PotentialSearch'])

        # Adding model 'SearchEmailerSender'
        db.create_table(u'domain_searchemailersender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search_aggregate_id', self.gf('django.db.models.fields.IntegerField')()),
            ('specified_location', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('from_name', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('subject', self.gf('django.db.models.fields.TextField')()),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('domain', ['SearchEmailerSender'])

        # Adding model 'AddApartmentToSearch'
        db.create_table(u'domain_addapartmenttosearch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartment_aggregate_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('is_available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lng', self.gf('django.db.models.fields.FloatField')()),
            ('broker_fee', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cats_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dogs_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('bedroom_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2, null=True, blank=True)),
            ('bathroom_count', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('sqfeet', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True)),
            ('listing_urls', self.gf('django.db.models.fields.TextField')(default='[]')),
            ('last_updated_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('contact_phone_number', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('contact_email_address', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('amenities', self.gf('django.db.models.fields.TextField')(default='{}', null=True, blank=True)),
        ))
        db.send_create_signal('domain', ['AddApartmentToSearch'])

        # Adding model 'SearchResult'
        db.create_table(u'domain_searchresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('result_aggregate_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('apartment_aggregate_id', self.gf('django.db.models.fields.IntegerField')()),
            ('search_aggregate_id', self.gf('django.db.models.fields.IntegerField')()),
            ('is_available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lng', self.gf('django.db.models.fields.FloatField')()),
            ('broker_fee', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('bedroom_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2, null=True, blank=True)),
            ('bathroom_count', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('sqfeet', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True)),
            ('listing_urls', self.gf('django.db.models.fields.TextField')(default='[]')),
            ('last_updated_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('contact_phone_number', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('contact_email_address', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('amenities', self.gf('django.db.models.fields.TextField')(default='{}', null=True, blank=True)),
            ('compliance_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('availability_contact_response', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('availability_last_response_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('availability_system_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('domain', ['SearchResult'])

        # Adding unique constraint on 'SearchResult', fields ['apartment_aggregate_id', 'search_aggregate_id']
        db.create_unique(u'domain_searchresult', ['apartment_aggregate_id', 'search_aggregate_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'SearchResult', fields ['apartment_aggregate_id', 'search_aggregate_id']
        db.delete_unique(u'domain_searchresult', ['apartment_aggregate_id', 'search_aggregate_id'])

        # Deleting model 'PotentialSearch'
        db.delete_table(u'domain_potentialsearch')

        # Deleting model 'SearchEmailerSender'
        db.delete_table(u'domain_searchemailersender')

        # Deleting model 'AddApartmentToSearch'
        db.delete_table(u'domain_addapartmenttosearch')

        # Deleting model 'SearchResult'
        db.delete_table(u'domain_searchresult')


    models = {
        'domain.addapartmenttosearch': {
            'Meta': {'object_name': 'AddApartmentToSearch'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amenities': ('django.db.models.fields.TextField', [], {'default': "'{}'", 'null': 'True', 'blank': 'True'}),
            'apartment_aggregate_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'bathroom_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bedroom_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'broker_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cats_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dogs_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated_date': ('django.db.models.fields.DateTimeField', [], {}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'listing_urls': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'sqfeet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'})
        },
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
            'description': ('django.db.models.fields.TextField', [], {}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'search_aggregate_id': ('django.db.models.fields.IntegerField', [], {}),
            'specified_location': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'subject': ('django.db.models.fields.TextField', [], {})
        },
        'domain.searchresult': {
            'Meta': {'unique_together': "(('apartment_aggregate_id', 'search_aggregate_id'),)", 'object_name': 'SearchResult'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amenities': ('django.db.models.fields.TextField', [], {'default': "'{}'", 'null': 'True', 'blank': 'True'}),
            'apartment_aggregate_id': ('django.db.models.fields.IntegerField', [], {}),
            'availability_contact_response': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'availability_last_response_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'availability_system_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'bathroom_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bedroom_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'broker_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'compliance_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'contact_email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated_date': ('django.db.models.fields.DateTimeField', [], {}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'listing_urls': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'result_aggregate_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'search_aggregate_id': ('django.db.models.fields.IntegerField', [], {}),
            'sqfeet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'})
        }
    }

    complete_apps = ['domain']