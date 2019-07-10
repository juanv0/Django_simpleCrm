# Generated by Django 2.2.3 on 2019-07-07 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64, verbose_name='Name of Account')),
                ('emai', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('industry', models.CharField(blank=True, choices=[('FINANCE', 'FINANCE'), ('HEALTHCARE', 'HEALTHCARE'), ('INSURANCE', 'INSURANCE'), ('LEGAL', 'LEGAL'), ('MANUFACTURING', 'MANUFACTURING'), ('PUBLISHING', 'PUBLISHING'), ('REAL ESTATE', 'REAL ESTATE'), ('SOFTWARE', 'SOFTWARE')], max_length=255, null=True, verbose_name='Industry Type')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('description', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('isActive', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20, verbose_name='Activity Status')),
            ],
        ),
        migrations.CreateModel(
            name='ContactSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20, verbose_name='Contact Status')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('isActive', models.BooleanField(default=False)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_account_contacts', to='crmapp.Account')),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.Contact')),
            ],
        ),
    ]
