# Generated by Django 3.1.4 on 2020-12-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0016_auto_20201218_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_expired_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
