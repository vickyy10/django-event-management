# Generated by Django 5.0.6 on 2024-06-19 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('peoplestrength', models.BigIntegerField()),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_admin.events')),
            ],
        ),
    ]