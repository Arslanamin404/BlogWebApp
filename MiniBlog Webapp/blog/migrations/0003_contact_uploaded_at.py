# Generated by Django 4.2.5 on 2023-11-05 07:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
