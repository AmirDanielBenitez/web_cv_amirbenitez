# Generated by Django 3.2.25 on 2024-04-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('linkedin', models.URLField()),
                ('whatsapp_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
