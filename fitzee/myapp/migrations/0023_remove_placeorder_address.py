# Generated by Django 3.2.9 on 2022-03-22 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_auto_20220321_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeorder',
            name='address',
        ),
    ]