# Generated by Django 4.1 on 2024-03-08 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artsforum', '0002_bid_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='user_created',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
