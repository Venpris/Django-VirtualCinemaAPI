# Generated by Django 4.2.7 on 2023-11-14 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='seat',
        ),
        migrations.AddField(
            model_name='movie',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='seat_number',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
    ]
