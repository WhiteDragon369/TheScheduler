# Generated by Django 4.2.6 on 2023-10-28 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='branch2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('mon', models.CharField(max_length=25)),
                ('tue', models.CharField(max_length=25)),
                ('wed', models.CharField(max_length=25)),
                ('thu', models.CharField(max_length=25)),
                ('fri', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='branch3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('mon', models.CharField(max_length=25)),
                ('tue', models.CharField(max_length=25)),
                ('wed', models.CharField(max_length=25)),
                ('thu', models.CharField(max_length=25)),
                ('fri', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='profs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=25)),
                ('branches', models.CharField(max_length=50)),
            ],
        ),
    ]
