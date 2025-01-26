# Generated by Django 5.1.5 on 2025-01-26 04:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kindergarten', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('Intern', 'Intern'), ('Junior', 'Junior'), ('Middle', 'Middle'), ('Manager', 'Manager'), ('Director', 'Director')], default='Intern', max_length=255)),
                ('experience', models.IntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': ('Employee',),
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('limit', models.IntegerField()),
                ('first_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_employee', to='participants.employee')),
                ('kindergarten', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='groups', to='kindergarten.kindergarten')),
                ('second_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_employee', to='participants.employee')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=2)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('kindergarten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='kindergarten.kindergarten')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children', to='participants.group')),
            ],
            options={
                'verbose_name': ('Child',),
                'verbose_name_plural': 'Children',
            },
        ),
        migrations.CreateModel(
            name='RepresentativeChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Parent', 'Parent'), ('Guardian', 'Guardian')], default='Parent', max_length=10)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='representatives', to='participants.child')),
                ('representative', models.ForeignKey(limit_choices_to={'ut': 1}, on_delete=django.db.models.deletion.PROTECT, related_name='children', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ('Child Representative',),
                'verbose_name_plural': 'Children Representatives',
            },
        ),
    ]
