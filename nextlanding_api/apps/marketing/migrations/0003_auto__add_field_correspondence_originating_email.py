# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    depends_on = (("communication_utils", "0001_initial"),)

    def forwards(self, orm):
        # Adding field 'Correspondence.originating_email'
        db.add_column(u'marketing_correspondence', 'originating_email',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['communication_utils.Email'], unique=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Correspondence.originating_email'
        db.delete_column(u'marketing_correspondence', 'originating_email_id')


    models = {
        u'communication_utils.email': {
            'Meta': {'unique_together': "(('message_id', 'sent_date'),)", 'object_name': 'Email'},
            'SPF': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'charsets': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dkim': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email_direction': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2'}),
            'envelope': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.TextField', [], {}),
            'headers': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_reply_to_message_id': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sender_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sent_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'spam_report': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'spam_score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'to': ('django.db.models.fields.TextField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'originating_email': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['communication_utils.Email']", 'unique': 'True'}),
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
