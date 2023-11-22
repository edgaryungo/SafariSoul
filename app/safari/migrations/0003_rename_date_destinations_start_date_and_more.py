# Generated by Django 4.2.5 on 2023-11-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safari', '0002_remove_culturalattraction_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destinations',
            old_name='date',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='destinations',
            name='duration_days',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='destinations',
            name='duration_nights',
            field=models.PositiveIntegerField(null=True),
        ),
    ]