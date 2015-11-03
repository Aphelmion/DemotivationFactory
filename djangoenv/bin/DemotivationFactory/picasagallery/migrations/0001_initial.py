# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demotivator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('demotivator_name', models.CharField(max_length=100)),
                ('demotivator_date', models.DateTimeField()),
                ('demotivator_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'demotivator',
            },
        ),
    ]
