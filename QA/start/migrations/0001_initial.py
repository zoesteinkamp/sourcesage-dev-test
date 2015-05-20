# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('answerer', models.CharField(unique=True, max_length=40)),
                ('post', models.TextField(max_length=3000)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('poster', models.CharField(unique=True, max_length=40)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=300)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.ForeignKey(to='start.Question'),
        ),
    ]
