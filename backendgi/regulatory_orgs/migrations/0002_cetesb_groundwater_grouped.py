# Generated by Django 5.1.1 on 2024-10-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_orgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cetesb',
            name='groundwater_grouped',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
