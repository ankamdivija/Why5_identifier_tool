# Generated by Django 3.0.4 on 2020-04-09 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200408_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='profile_pic',
            field=models.ImageField(blank=True, default='users/user.png', null=True, upload_to='users/'),
        ),
    ]