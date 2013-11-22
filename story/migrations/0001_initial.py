# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Line'
        db.create_table(u'story_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'story', ['Line'])

        # Adding model 'ZomatoItem'
        db.create_table(u'story_zomatoitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('recommendations', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rating_scale', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rating_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('highlights', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cuisines', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('opening_times', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('happy_hours', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('buffet', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('images', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'story', ['ZomatoItem'])


    def backwards(self, orm):
        # Deleting model 'Line'
        db.delete_table(u'story_line')

        # Deleting model 'ZomatoItem'
        db.delete_table(u'story_zomatoitem')


    models = {
        u'story.line': {
            'Meta': {'object_name': 'Line'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'story.zomatoitem': {
            'Meta': {'object_name': 'ZomatoItem'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'buffet': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cuisines': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'happy_hours': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'highlights': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opening_times': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rating_scale': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rating_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recommendations': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['story']