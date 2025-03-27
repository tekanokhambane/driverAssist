# Generated by Django 5.1.7 on 2025-03-27 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('plate_number', models.CharField(max_length=15, unique=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('plate_number', models.CharField(max_length=15, unique=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.driver')),
            ],
        ),
    ]
