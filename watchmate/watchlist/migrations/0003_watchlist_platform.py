# Generated by Django 4.2.2 on 2023-06-28 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0002_streamplatform_rename_movie_watchlist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='watchlist.streamplatform'),
        ),
    ]
