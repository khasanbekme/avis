# Generated by Django 5.0.2 on 2024-02-09 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_charity_disaster_text_donation_media_story'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charity',
            options={'verbose_name_plural': 'Charities'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name_plural': 'Media'},
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'Stories'},
        ),
    ]
