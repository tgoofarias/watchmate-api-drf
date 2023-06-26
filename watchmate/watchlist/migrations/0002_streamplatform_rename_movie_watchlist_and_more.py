# Generated by Django 4.2.2 on 2023-06-26 18:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamPlatform',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('about', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Movie',
            new_name='WatchList',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='name',
            new_name='title',
        ),
    ]