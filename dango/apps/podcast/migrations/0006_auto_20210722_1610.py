# Generated by Django 3.1.13 on 2021-07-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0005_auto_20210317_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='excerpt',
            field=models.TextField(default='excerpt'),
        ),
    ]
