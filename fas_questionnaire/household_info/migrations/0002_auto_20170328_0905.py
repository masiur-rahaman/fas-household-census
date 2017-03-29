# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('household_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseholdMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('relationship', models.CharField(max_length=40)),
                ('marital_status', models.CharField(max_length=40)),
                ('occupation', models.CharField(max_length=100)),
                ('place_of_work', models.CharField(max_length=100)),
                ('literacy_status', models.CharField(max_length=40)),
                ('education_level', models.CharField(max_length=40)),
                ('enrolled_institution', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='household',
            name='id',
        ),
        migrations.AddField(
            model_name='household',
            name='Household_number',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='household',
            name='address',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='household',
            name='age',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='household',
            name='year_of_migration',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='householdmembers',
            name='Household_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='household_info.Household'),
        ),
    ]