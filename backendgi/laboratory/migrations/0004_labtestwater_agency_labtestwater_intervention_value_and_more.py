# Generated by Django 5.1.1 on 2024-11-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0003_labtestwater_delete_lab_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestwater',
            name='agency',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='labtestwater',
            name='intervention_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='labtestwater',
            name='substance_agency',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
