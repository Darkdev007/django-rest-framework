# Generated by Django 4.1 on 2022-09-16 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0008_rename_avg_ratings_review_avg_rating_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='number_ratings',
            new_name='number_rating',
        ),
    ]
