# Generated by Django 4.0.3 on 2022-04-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_delete_city_delete_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='price',
            field=models.IntegerField(),
        ),
    ]
