# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'blogengine_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('title_en', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('title_ru', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('teaser', self.gf('django.db.models.fields.TextField')()),
            ('teaser_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('teaser_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(default=u'personal-development', max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'blogengine', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'blogengine_post')


    models = {
        u'blogengine.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'tag': ('django.db.models.fields.CharField', [], {'default': "u'personal-development'", 'max_length': '200'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'teaser_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'teaser_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'title_en': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['blogengine']