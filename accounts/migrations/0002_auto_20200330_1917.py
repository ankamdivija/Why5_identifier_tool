# Generated by Django 3.0.4 on 2020-03-30 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='UserDetail',
        ),
    ]
