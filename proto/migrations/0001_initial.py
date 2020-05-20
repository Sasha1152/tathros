# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-20 22:31
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, default='/static/categories/placeholder.png', null=True, upload_to=django.core.files.storage.FileSystemStorage(location='/static/categories'))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('ip', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('ip', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=255)),
                ('image', models.ImageField(upload_to='proto/gallery')),
                ('categories', models.ManyToManyField(to='proto.Category')),
            ],
            options={
                'ordering': ['?'],
            },
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('company_name', models.CharField(max_length=255)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('vat_number', models.CharField(max_length=100)),
                ('email_notification_code', models.CharField(blank=True, max_length=100)),
                ('birth_date', models.DateField()),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_pictures')),
                ('news_letter', models.BooleanField()),
                ('is_mock', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(to='proto.Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PhotographerSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('program', models.CharField(max_length=100)),
                ('start', models.DateField(auto_now=True)),
                ('end', models.DateField(auto_now=True)),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='proto.Photographer')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('likes', models.IntegerField()),
                ('photos', models.IntegerField()),
                ('price', models.IntegerField()),
                ('is_premium', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='photographersubscription',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='proto.Subscription'),
        ),
        migrations.AddField(
            model_name='photo',
            name='photographer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='proto.Photographer'),
        ),
        migrations.AddField(
            model_name='like',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='likes', to='proto.Photo'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='impression',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='impressions', to='proto.Photo'),
        ),
        migrations.AddField(
            model_name='impression',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='photographers',
            field=models.ManyToManyField(blank=True, related_query_name='category', to='proto.Photographer'),
        ),
        migrations.AddField(
            model_name='category',
            name='photos',
            field=models.ManyToManyField(blank=True, related_query_name='category', to='proto.Photo'),
        ),
    ]
