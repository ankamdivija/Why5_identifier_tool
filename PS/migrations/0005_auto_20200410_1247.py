# Generated by Django 3.0.4 on 2020-04-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PS', '0004_auto_20200410_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemstatement',
            name='category',
        ),
        migrations.AddField(
            model_name='problemstatement',
            name='category',
            field=models.ManyToManyField(related_name='category', to='PS.Category'),
        ),
    ]
