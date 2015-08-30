# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Post.slug'
        db.alter_column(u'blogengine_post', 'slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255))
        # Removing index on 'Post', fields ['slug']
        db.delete_index(u'blogengine_post', ['slug'])

        # Adding unique constraint on 'Post', fields ['slug']
        db.create_unique(u'blogengine_post', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Post', fields ['slug']
        db.delete_unique(u'blogengine_post', ['slug'])

        # Adding index on 'Post', fields ['slug']
        db.create_index(u'blogengine_post', ['slug'])


        # Changing field 'Post.slug'
        db.alter_column(u'blogengine_post', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    models = {
        u'blogengine.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'tag': ('django.db.models.fields.CharField', [], {'default': "u'personal-development'", 'max_length': '200'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blogengine']