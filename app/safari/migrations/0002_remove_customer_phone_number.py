# Generated by Django 4.2.5 on 2023-11-22 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safari', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
    ]
