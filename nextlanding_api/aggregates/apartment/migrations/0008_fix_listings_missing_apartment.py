# -*- coding: utf-8 -*-
import datetime
from django.conf import settings
from south.db import db
from south.exceptions import BrokenMigration
from south.v2 import DataMigration
from django.db import models
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.apartment.signals import adopted_listing


class Migration(DataMigration):
    depends_on = (("listing", "0019_auto__del_field_listing_is_dead__add_field_listing_deleted_reason"),)

    def forwards(self, orm):
      settings.CELERY_ALWAYS_EAGER = True

      if adopted_listing.version == 1:
        listings_without_apartment = orm['listing.Listing'].objects.filter(apartment__isnull=True)
        for l in listings_without_apartment:
          apartment_service.adopt_listing(l)
      else:
        raise Exception('Unknown adopted_listing version: {0}'.format(adopted_listing.version))

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'amenity.amenity': {
            'Meta': {'object_name': 'Amenity'},
            'aliases': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'apartment.amenity': {
            'Meta': {'unique_together': "(('apartment', 'amenity_type'),)", 'object_name': 'Amenity'},
            'amenity_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'apartment_instance'", 'to': u"orm['amenity.Amenity']"}),
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'amenities'", 'to': u"orm['apartment.Apartment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
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
        u'listing.amenity': {
            'Meta': {'unique_together': "(('listing', 'amenity_type'),)", 'object_name': 'Amenity'},
            'amenity_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'listing_instance'", 'to': u"orm['amenity.Amenity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'listing': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'amenities'", 'to': u"orm['listing.Listing']"})
        },
        u'listing.listing': {
            'Meta': {'object_name': 'Listing'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'listings'", 'null': 'True', 'to': u"orm['apartment.Apartment']"}),
            'bathroom_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bedroom_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'broker_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted_reason': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'formatted_address': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'listing_source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listing_source.ListingSource']"}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'posted_date': ('django.db.models.fields.DateTimeField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'sqfeet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '8000'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'listing_source.listingsource': {
            'Meta': {'object_name': 'ListingSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'public_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'trusted_geo_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['listing', 'apartment']
    symmetrical = True
