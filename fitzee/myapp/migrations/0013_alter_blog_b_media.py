# Generated by Django 3.2.9 on 2022-03-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20220302_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='b_media',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
