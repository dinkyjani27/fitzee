# Generated by Django 4.0 on 2022-02-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='e_reps',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='exercise',
            name='e_sets',
            field=models.TextField(default=''),
        ),
    ]
