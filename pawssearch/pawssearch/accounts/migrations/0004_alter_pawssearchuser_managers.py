# Generated by Django 5.1.1 on 2024-09-20 17:32

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_pawssearchuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='pawssearchuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
