# Generated by Django 4.0.3 on 2022-05-05 19:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0015_alter_hobbylist_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbylist',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 19, 40, 7, 449598, tzinfo=utc)),
        ),
    ]