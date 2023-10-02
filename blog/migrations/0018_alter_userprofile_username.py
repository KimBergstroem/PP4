# Generated by Django 3.2.21 on 2023-10-01 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20231001_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='User', max_length=15, validators=[django.core.validators.MaxLengthValidator(limit_value=15)]),
        ),
    ]