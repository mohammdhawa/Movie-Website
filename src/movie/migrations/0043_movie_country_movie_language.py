# Generated by Django 4.1.2 on 2022-12-18 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0042_remove_movie_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.country'),
        ),
        migrations.AddField(
            model_name='movie',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.language'),
        ),
    ]
