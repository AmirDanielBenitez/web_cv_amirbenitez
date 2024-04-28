# Generated by Django 3.2.25 on 2024-04-28 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='platform',
            field=models.CharField(choices=[('web', 'Web'), ('app', 'Mobile')], default='app', max_length=10),
            preserve_default=False,
        ),
    ]