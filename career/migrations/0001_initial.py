# Generated by Django 5.0.6 on 2024-06-20 08:12

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='careermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('resume', models.ImageField(upload_to='resume')),
                ('comment', models.TextField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_admin.careeravailability')),
            ],
        ),
    ]