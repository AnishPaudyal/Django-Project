# Generated by Django 4.0.3 on 2022-04-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_profile_avatar_remove_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
    ]
