# Generated by Django 2.2.12 on 2022-06-13 19:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0011_alter_hobbylist_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='hobbylist',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 19, 54, 16, 983580, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hobbylist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
