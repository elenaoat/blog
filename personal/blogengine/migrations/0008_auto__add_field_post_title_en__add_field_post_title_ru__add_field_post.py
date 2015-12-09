# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.title_en'
        db.add_column(u'blogengine_post', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.title_ru'
        db.add_column(u'blogengine_post', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.teaser_en'
        db.add_column(u'blogengine_post', 'teaser_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.teaser_ru'
        db.add_column(u'blogengine_post', 'teaser_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.text_en'
        db.add_column(u'blogengine_post', 'text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.text_ru'
        db.add_column(u'blogengine_post', 'text_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Post.title'
        db.alter_column(u'blogengine_post', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

    def backwards(self, orm):
        # Deleting field 'Post.title_en'
        db.delete_column(u'blogengine_post', 'title_en')

        # Deleting field 'Post.title_ru'
        db.delete_column(u'blogengine_post', 'title_ru')

        # Deleting field 'Post.teaser_en'
        db.delete_column(u'blogengine_post', 'teaser_en')

        # Deleting field 'Post.teaser_ru'
        db.delete_column(u'blogengine_post', 'teaser_ru')

        # Deleting field 'Post.text_en'
        db.delete_column(u'blogengine_post', 'text_en')

        # Deleting field 'Post.text_ru'
        db.delete_column(u'blogengine_post', 'text_ru')


        # Changing field 'Post.title'
        db.alter_column(u'blogengine_post', 'title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['blogengine']