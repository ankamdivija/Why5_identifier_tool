# Generated by Django 3.0.4 on 2020-04-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200405_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='username',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='proffesion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
