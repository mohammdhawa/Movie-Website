# Generated by Django 4.1.2 on 2022-12-18 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0041_remove_movie_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='language',
        ),
    ]
