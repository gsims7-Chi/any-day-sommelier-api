# Generated by Django 2.1 on 2018-08-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('any_day_sommelier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='wines',
            field=models.ManyToManyField(through='any_day_sommelier.Pairing', to='any_day_sommelier.Wine'),
        ),
    ]
