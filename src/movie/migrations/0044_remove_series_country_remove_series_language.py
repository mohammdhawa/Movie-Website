# Generated by Django 4.1.2 on 2022-12-18 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0043_movie_country_movie_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='country',
        ),
        migrations.RemoveField(
            model_name='series',
            name='language',
        ),
    ]
