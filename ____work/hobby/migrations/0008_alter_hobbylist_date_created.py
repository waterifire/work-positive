# Generated by Django 4.0.3 on 2022-04-30 16:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0007_alter_hobbylist_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbylist',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 30, 16, 17, 14, 434674, tzinfo=utc)),
        ),
    ]
