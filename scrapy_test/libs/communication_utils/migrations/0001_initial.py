# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Email'
        db.create_table(u'communication_utils_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headers', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('to', self.gf('django.db.models.fields.TextField')()),
            ('from_address', self.gf('django.db.models.fields.TextField')()),
            ('cc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('subject', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('dkim', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
            ('SPF', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
            ('envelope', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
            ('charsets', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('spam_score', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('spam_report', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('message_id', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('in_reply_to_message_id', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('email_direction', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2)),
            ('sent_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'communication_utils', ['Email'])

        # Adding unique constraint on 'Email', fields ['message_id', 'sent_date']
        db.create_unique(u'communication_utils_email', ['message_id', 'sent_date'])


    def backwards(self, orm):
        # Removing unique constraint on 'Email', fields ['message_id', 'sent_date']
        db.delete_unique(u'communication_utils_email', ['message_id', 'sent_date'])

        # Deleting model 'Email'
        db.delete_table(u'communication_utils_email')


    models = {
        u'communication_utils.email': {
            'Meta': {'unique_together': "(('message_id', 'sent_date'),)", 'object_name': 'Email'},
            'SPF': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'cc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'charsets': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dkim': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'email_direction': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2'}),
            'envelope': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.TextField', [], {}),
            'headers': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_reply_to_message_id': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['communication_utils']