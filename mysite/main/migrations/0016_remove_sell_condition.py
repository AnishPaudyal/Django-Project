# Generated by Django 4.0.3 on 2022-04-10 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_sell_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='condition',
        ),
    ]
