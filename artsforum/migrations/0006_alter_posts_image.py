# Generated by Django 4.1 on 2024-03-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artsforum', '0005_userrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
