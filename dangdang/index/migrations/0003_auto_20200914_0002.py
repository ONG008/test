# Generated by Django 2.0.6 on 2020-09-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_tclass_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbook',
            name='content_introduction',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
