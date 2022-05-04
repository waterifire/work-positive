# Generated by Django 4.0.3 on 2022-05-04 20:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_setup', '0007_alter_quizsetup_created_tmmasetup'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmmasetup',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 20, 55, 21, 895685, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='tmmasetup',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='wordlesetup',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 20, 55, 21, 895685, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='wordlesetup',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='quizsetup',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 20, 55, 21, 894690, tzinfo=utc)),
        ),
    ]
