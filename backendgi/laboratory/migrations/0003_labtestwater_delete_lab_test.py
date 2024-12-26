# Generated by Django 5.1.1 on 2024-11-18 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0002_remove_lab_test_substance'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTestWater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(max_length=30)),
                ('sample_type', models.CharField(max_length=30)),
                ('sample_name', models.CharField(max_length=30)),
                ('substance', models.CharField(max_length=300)),
                ('result', models.FloatField()),
                ('under_limit', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Lab_test',
        ),
    ]