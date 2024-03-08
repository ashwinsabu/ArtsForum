# Generated by Django 4.1 on 2024-03-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('user_created', models.IntegerField()),
            ],
        ),
    ]
