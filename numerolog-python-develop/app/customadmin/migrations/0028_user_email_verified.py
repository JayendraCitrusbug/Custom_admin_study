# Generated by Django 3.1.4 on 2021-02-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0027_user_password_reset_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]