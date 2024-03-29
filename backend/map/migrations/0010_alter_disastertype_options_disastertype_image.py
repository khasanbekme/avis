# Generated by Django 5.0.2 on 2024-02-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0009_remove_disaster_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disastertype',
            options={'verbose_name_plural': 'Disaster Types'},
        ),
        migrations.AddField(
            model_name='disastertype',
            name='image',
            field=models.ImageField(blank=True, upload_to='disaster-types/'),
        ),
    ]
