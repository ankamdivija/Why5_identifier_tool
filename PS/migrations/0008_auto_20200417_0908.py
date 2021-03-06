# Generated by Django 3.0.5 on 2020-04-17 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200409_0546'),
        ('PS', '0007_auto_20200414_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='givenBy',
        ),
        migrations.AddField(
            model_name='answer',
            name='givenBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PS_givenby', to='accounts.UserDetail'),
        ),
        migrations.RemoveField(
            model_name='problemstatement',
            name='category',
        ),
        migrations.AddField(
            model_name='problemstatement',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='PS.Category'),
        ),
    ]
