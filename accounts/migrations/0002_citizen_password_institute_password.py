# Generated by Django 5.1.6 on 2025-02-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='institute',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
