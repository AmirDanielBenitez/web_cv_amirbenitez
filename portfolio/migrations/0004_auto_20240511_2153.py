# Generated by Django 3.2.25 on 2024-05-11 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20240511_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='code_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
