# Generated by Django 4.1 on 2024-03-08 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid_posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('amount_initial', models.IntegerField()),
                ('amount_final', models.IntegerField()),
                ('time_limit', models.DateTimeField()),
                ('Status', models.IntegerField()),
                ('user_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_bids', to=settings.AUTH_USER_MODEL)),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_bids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
