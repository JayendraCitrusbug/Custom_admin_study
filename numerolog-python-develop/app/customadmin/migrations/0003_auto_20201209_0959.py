# Generated by Django 3.1.4 on 2020-12-09 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0002_auto_20201209_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('note', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Inquiry',
                'verbose_name_plural': 'Inquiries',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='InquiryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('inquiry_type', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Inquiry Type',
                'verbose_name_plural': 'Inquiry Types',
                'ordering': ['-created_at'],
            },
        ),
        migrations.DeleteModel(
            name='Enquiry',
        ),
        migrations.DeleteModel(
            name='EnquiryType',
        ),
        migrations.AddField(
            model_name='inquiry',
            name='inquiry_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customadmin.inquirytype'),
        ),
    ]