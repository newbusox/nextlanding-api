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
            ('changed_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('broker_fee', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cats_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dogs_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('bedroom_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2, null=True, blank=True)),
            ('bathroom_count', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('sqfeet', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True)),
            ('listing_urls', self.gf('django.db.models.fields.TextField')(default='[]')),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('contact_phone_number', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('contact_email_address', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('amenities', self.gf('django.db.models.fields.TextField')(default='{}', null=True, blank=True)),
        ))
        db.send_create_signal('domain', ['AddApartmentToSearch'])


    def backwards(self, orm):
        # Deleting model 'PotentialSearch'
        db.delete_table(u'domain_potentialsearch')

        # Deleting model 'SearchEmailerSender'
        db.delete_table(u'domain_searchemailersender')

        # Deleting model 'AddApartmentToSearch'
        db.delete_table(u'domain_addapartmenttosearch')


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
            'changed_date': ('django.db.models.fields.DateTimeField', [], {}),
            'contact_email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dogs_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        }
    }

    complete_apps = ['domain']