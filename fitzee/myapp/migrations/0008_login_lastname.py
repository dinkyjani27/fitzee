# Generated by Django 3.2.9 on 2022-02-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_login_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='lastname',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
