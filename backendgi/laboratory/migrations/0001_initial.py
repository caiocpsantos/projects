# Generated by Django 5.1.1 on 2024-10-24 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regulatory_orgs', '0002_cetesb_groundwater_grouped'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(max_length=30)),
                ('sample_type', models.CharField(blank=True, max_length=30, null=True)),
                ('sample_name', models.CharField(blank=True, max_length=30, null=True)),
                ('result', models.FloatField(blank=True, null=True)),
                ('math_symbol', models.CharField(blank=True, max_length=2, null=True)),
                ('unit', models.CharField(blank=True, max_length=10, null=True)),
                ('substance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='regulatory_orgs.substance')),
            ],
        ),
    ]