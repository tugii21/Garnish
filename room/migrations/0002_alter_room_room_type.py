# Generated by Django 4.2.11 on 2024-03-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('1', 'Single Room'), ('2', 'Double Room'), ('3', 'Ensuite Room')], default='1', max_length=2),
        ),
    ]
