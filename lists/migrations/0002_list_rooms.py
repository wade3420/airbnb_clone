# Generated by Django 3.1 on 2020-09-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='rooms',
            field=models.ManyToManyField(blank=True, to='rooms.Room'),
        ),
    ]
