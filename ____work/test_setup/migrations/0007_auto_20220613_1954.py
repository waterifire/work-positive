# Generated by Django 2.2.12 on 2022-06-13 19:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_setup', '0006_alter_quizsetup_created_wordlesetup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizsetup',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 19, 54, 16, 984772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quizsetup',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wordlesetup',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]