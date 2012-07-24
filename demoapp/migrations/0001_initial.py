# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InterestingPerson'
        db.create_table('demoapp_interestingperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('twitter_username', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('follow_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('picture_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('demoapp', ['InterestingPerson'])


    def backwards(self, orm):
        # Deleting model 'InterestingPerson'
        db.delete_table('demoapp_interestingperson')


    models = {
        'demoapp.interestingperson': {
            'Meta': {'object_name': 'InterestingPerson'},
            'follow_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'picture_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['demoapp']