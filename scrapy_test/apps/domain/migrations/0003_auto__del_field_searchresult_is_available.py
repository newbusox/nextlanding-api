# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SearchResult.is_available'
        db.delete_column(u'domain_searchresult', 'is_available')


    def backwards(self, orm):
        # Adding field 'SearchResult.is_available'
        db.add_column(u'domain_searchresult', 'is_available',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        'domain.addapartmenttosearch': {
            'Meta': {'object_name': 'AddApartmentToSearch'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amenities': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'apartment_aggregate_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'bathroom_count': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'bedroom_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2'}),
            'broker_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cats_allowed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dogs_allowed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated_date': ('django.db.models.fields.DateTimeField', [], {}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'listing_urls': ('jsonfield.fields.JSONField', [], {'default': '[]'}),
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
            'amenities': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
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
            'last_updated_date': ('django.db.models.fields.DateTimeField', [], {}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'listing_urls': ('jsonfield.fields.JSONField', [], {'default': '[]'}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'result_aggregate_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'search_aggregate_id': ('django.db.models.fields.IntegerField', [], {}),
            'sqfeet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'})
        }
    }

    complete_apps = ['domain']