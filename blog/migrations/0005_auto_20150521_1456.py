# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_entry_body_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', django_markdown.models.MarkdownField()),
                ('body_html', models.TextField(null=True, editable=False, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
            },
        ),
        migrations.RemoveField(
            model_name='entry',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
