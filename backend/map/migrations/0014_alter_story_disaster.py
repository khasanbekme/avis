# Generated by Django 5.0.2 on 2024-02-10 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0013_story_disaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='disaster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='map.disaster'),
        ),
    ]
