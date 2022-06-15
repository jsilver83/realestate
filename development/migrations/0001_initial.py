# Generated by Django 3.2.13 on 2022-06-15 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(null=True, verbose_name='Address')),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Mobile')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Phone')),
                ('nationality', django_countries.fields.CountryField(max_length=2, null=True, verbose_name='Nationality')),
                ('city', models.CharField(max_length=250, null=True, verbose_name='City')),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], default='M', max_length=2, verbose_name='Gender')),
                ('photo', models.ImageField(upload_to='', verbose_name='Personal Photo')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='Project Name')),
                ('about', models.CharField(max_length=250, null=True, verbose_name='About')),
                ('state', models.CharField(choices=[('NEW', 'New'), ('UNDER-CONSTRUCTION', 'Under-Construction'), ('COMPLETE', 'Complete'), ('INCOMPLETE', 'Incomplete'), ('AVAILABLE', 'Available'), ('UNAVAILABLE', 'Unavailable')], default='NEW', max_length=20, verbose_name='State of the Project')),
                ('type', models.CharField(choices=[('VILLA', 'Villa'), ('BUILDING', 'Apartment Building'), ('COMPLEX', 'Residential Complex'), ('COMMERCIAL', 'Commercial'), ('INDUSTRIAL', 'Industrial'), ('LAND', 'Lands')], default='VILLA', max_length=20, verbose_name='Type of the Project')),
                ('location', models.TextField(null=True, verbose_name='Location')),
                ('area', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Area (square meters)')),
                ('friends', models.TextField(blank=True, null=True, verbose_name='Friends')),
                ('district', models.CharField(blank=True, max_length=250, null=True, verbose_name='District')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='development.project', verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='development.client')),
                ('is_company', models.BooleanField(verbose_name='Is a Company?')),
                ('company_name', models.CharField(max_length=250, null=True, verbose_name='Company Name')),
                ('commercial_license', models.FileField(upload_to='', verbose_name='Commercial License')),
                ('company_website', models.CharField(max_length=512, null=True, verbose_name='Company Website ')),
            ],
            bases=('development.client',),
        ),
        migrations.CreateModel(
            name='SubStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('done', models.BooleanField(verbose_name='Done')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='development.stage', verbose_name='Stage')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_date', models.DateTimeField(auto_now_add=True, verbose_name='Subscription Date')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='development.client', verbose_name='Client')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='development.project', verbose_name='Project')),
                ('referral', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to='development.client', verbose_name='Referral')),
            ],
        ),
        migrations.CreateModel(
            name='StageUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_text', models.TextField(null=True, verbose_name='Update Text')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='Update Date')),
                ('sub_stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='development.substage', verbose_name='Sub Stage')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, null=True, upload_to='', verbose_name='media')),
                ('stage_update', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='development.stageupdate', verbose_name='Stage Update')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='development.developer', verbose_name='developer'),
        ),
    ]