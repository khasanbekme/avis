# Generated by Django 5.0.2 on 2024-02-10 04:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0012_merge_20240210_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='disaster',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='map.disaster'),
            preserve_default=False,
        ),
    ]
