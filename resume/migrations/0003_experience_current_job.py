# Generated by Django 3.2.25 on 2024-04-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20240428_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='current_job',
            field=models.BooleanField(default=False),
        ),
    ]
