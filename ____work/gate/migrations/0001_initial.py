# Generated by Django 2.2.12 on 2022-06-13 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, help_text='not email password, random one', max_length=100, null=True)),
                ('job_title', models.CharField(blank=True, max_length=100, null=True)),
                ('job_description', models.CharField(blank=True, max_length=100, null=True)),
                ('like1', models.CharField(blank=True, max_length=100, null=True)),
                ('like2', models.CharField(blank=True, max_length=100, null=True)),
                ('like3', models.CharField(blank=True, max_length=100, null=True)),
                ('like4', models.CharField(blank=True, max_length=100, null=True)),
                ('hobby1', models.CharField(blank=True, max_length=100, null=True)),
                ('hobby2', models.CharField(blank=True, max_length=100, null=True)),
                ('hobby3', models.CharField(blank=True, max_length=100, null=True)),
                ('hobby4', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
