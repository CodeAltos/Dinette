# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user_groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=110)),
                ('description', models.TextField(default=b'')),
                ('ordering', models.PositiveIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('moderated_by', models.ManyToManyField(related_name='moderaters', to=settings.AUTH_USER_MODEL)),
                ('posted_by', models.ForeignKey(related_name='cposted', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('ordering', '-created_on'),
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='DinetteUserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_activity', models.DateTimeField(auto_now_add=True)),
                ('last_session_activity', models.DateTimeField(auto_now_add=True)),
                ('userrank', models.CharField(default=b'Junior Member', max_length=30)),
                ('last_posttime', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(null=True, upload_to=b'dinette/files', blank=True)),
                ('signature', models.CharField(max_length=1000, null=True, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('is_subscribed_to_digest', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ftopics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=999)),
                ('slug', models.SlugField(max_length=200)),
                ('message', markupfield.fields.MarkupField()),
                ('file', models.FileField(default=b'', null=True, upload_to=b'dinette/files', blank=True)),
                #('message_markup_type', models.CharField(default=b'plain', max_length=30, choices=[(b'', b'--'), (b'html', b'html'), (b'plain', b'plain'), (b'restructuredtext', b'restructuredtext')])),
                #('_message_rendered', models.TextField(editable=False)),
                ('attachment_type', models.CharField(default=b'nofile', max_length=20)),
                ('filename', models.CharField(default=b'dummyname.txt', max_length=100)),
                ('viewcount', models.IntegerField(default=0)),
                ('replies', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('last_reply_on', models.DateTimeField(auto_now_add=True)),
                ('num_replies', models.PositiveSmallIntegerField(default=0)),
                ('announcement_flag', models.BooleanField(default=False)),
                ('is_closed', models.BooleanField(default=False)),
                ('is_sticky', models.BooleanField(default=False)),
                ('is_hidden', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='dinette.Category')),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('subscribers', models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-is_sticky', '-last_reply_on'),
                'get_latest_by': 'created_on',
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.CreateModel(
            name='NavLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Navigation Link',
                'verbose_name_plural': 'Navigation Links',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', markupfield.fields.MarkupField()),
                ('file', models.FileField(default=b'', null=True, upload_to=b'dinette/files', blank=True)),
                #('message_markup_type', models.CharField(default=b'plain', max_length=30, choices=[(b'', b'--'), (b'html', b'html'), (b'plain', b'plain'), (b'restructuredtext', b'restructuredtext')])),
                #('_message_rendered', models.TextField(editable=False)),
                ('attachment_type', models.CharField(default=b'nofile', max_length=20)),
                ('filename', models.CharField(default=b'dummyname.txt', max_length=100)),
                ('reply_number', models.SmallIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(to='dinette.Ftopics')),
            ],
            options={
                'ordering': ('created_on',),
                'get_latest_by': ('created_on',),
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replies',
            },
        ),
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tag_line', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SuperCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
                ('ordering', models.PositiveIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('accessgroups', models.ManyToManyField(related_name='can_access_forums', to='user_groups.Group')),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-ordering', 'created_on'),
                'verbose_name': 'Super Category',
                'verbose_name_plural': 'Super Categories',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='super_category',
            field=models.ForeignKey(to='dinette.SuperCategory'),
        ),
    ]
