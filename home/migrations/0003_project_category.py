# Generated by Django 3.1.7 on 2021-03-23 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, choices=[('rector', 'rector'), ('raster', 'raster'), ('ui', 'ui'), ('printing', 'printing')], max_length=300),
        ),
    ]
