# Generated by Django 3.1.4 on 2020-12-09 06:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('enquiry_type', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Enquiry Type',
                'verbose_name_plural': 'Enquiry Types',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='testimonials', verbose_name='testimonial logo')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('testimonial_text', models.TextField(blank=True, default='', max_length=500, null=True)),
                ('designition', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('note', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('enquiry_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customadmin.enquirytype')),
            ],
            options={
                'verbose_name': 'Enquiry',
                'verbose_name_plural': 'Enquiries',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('username', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('profile_image', models.ImageField(blank=True, default='sample.jpg', null=True, upload_to='profile_image', verbose_name='Profile Image')),
                ('customer_id', models.CharField(blank=True, max_length=255, verbose_name='Customer Id')),
                ('language', models.CharField(blank=True, max_length=40)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Unique Id')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-created_at'],
            },
        ),
    ]
