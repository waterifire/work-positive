# Generated by Django 4.0.3 on 2022-04-30 16:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compliment', '0010_alter_compliment_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compliment',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 4, 30, 16, 18, 23, 939537, tzinfo=utc)),
        ),
    ]