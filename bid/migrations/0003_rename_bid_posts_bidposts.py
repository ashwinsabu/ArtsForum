# Generated by Django 4.1 on 2024-03-28 20:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bid', '0002_alter_bid_posts_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bid_posts',
            new_name='BidPosts',
        ),
    ]
