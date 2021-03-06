# Generated by Django 3.0.4 on 2020-04-12 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PS', '0005_auto_20200410_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='a_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_parent', to='PS.Answer'),
        ),
        migrations.AddField(
            model_name='problemstatement',
            name='visibility',
            field=models.CharField(choices=[('E', 'Everyone'), ('M', 'Only Me')], default=True, max_length=20),
            preserve_default=False,
        ),
    ]
