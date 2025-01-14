# Generated by Django 5.0.7 on 2024-07-30 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orbituaries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField()),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('submission_date', models.DateField(default=datetime.datetime.now)),
                ('slug', models.CharField(blank=True, max_length=255, unique=True)),
            ],
        ),
    ]
