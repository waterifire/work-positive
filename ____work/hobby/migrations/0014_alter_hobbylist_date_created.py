# Generated by Django 4.0.3 on 2022-05-04 20:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0013_alter_hobbylist_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbylist',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 20, 56, 4, 444837, tzinfo=utc)),
        ),
    ]
