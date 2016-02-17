# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=70)),
                ('review', models.TextField(blank=True, null=True)),
                ('date_reviewed', models.DateTimeField(blank=True, null=True)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
