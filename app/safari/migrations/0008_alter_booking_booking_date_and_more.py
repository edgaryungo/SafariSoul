# Generated by Django 4.2.5 on 2023-11-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safari', '0007_alter_destination_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tourpackage',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]