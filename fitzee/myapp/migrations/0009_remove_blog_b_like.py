# Generated by Django 3.2.9 on 2022-02-25 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_login_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='b_like',
        ),
    ]
