# Generated by Django 2.0.6 on 2020-09-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tclass',
            name='level',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
