# Generated by Django 3.2.9 on 2022-02-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_blog_b_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_id', models.CharField(blank=True, max_length=30)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
