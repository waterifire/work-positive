# Generated by Django 4.0.3 on 2022-04-29 08:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='allUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HobbyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbylist_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 4, 29, 8, 4, 4, 98360, tzinfo=utc))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hobby.allusers')),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hobby.hobbylist')),
                ('hobby_user', models.ManyToManyField(to='hobby.allusers')),
            ],
        ),
    ]
