# Generated by Django 3.2.9 on 2022-03-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20220309_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='calories2',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diet',
            name='d_name2',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
