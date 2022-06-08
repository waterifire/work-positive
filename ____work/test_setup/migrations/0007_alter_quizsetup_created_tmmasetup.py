# Generated by Django 4.0.3 on 2022-05-04 20:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_setup', '0006_alter_quizsetup_created_wordlesetup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizsetup',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 20, 48, 11, 110737, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='TmmaSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(blank=True, max_length=10, null=True)),
                ('q2', models.CharField(blank=True, max_length=10, null=True)),
                ('q3', models.CharField(blank=True, max_length=10, null=True)),
                ('q4', models.CharField(blank=True, max_length=10, null=True)),
                ('q5', models.CharField(blank=True, max_length=10, null=True)),
                ('q6', models.CharField(blank=True, max_length=10, null=True)),
                ('quiz_about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]