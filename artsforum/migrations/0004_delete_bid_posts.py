# Generated by Django 4.1 on 2024-03-08 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artsforum', '0003_alter_posts_user_created'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bid_posts',
        ),
    ]
