# Generated by Django 4.2.6 on 2023-10-29 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
