# Generated by Django 3.2.25 on 2024-04-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20240428_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='main_skill',
            field=models.BooleanField(default=False),
        ),
    ]
