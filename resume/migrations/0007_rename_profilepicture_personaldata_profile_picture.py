# Generated by Django 3.2.25 on 2024-05-02 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_personaldata_profilepicture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaldata',
            old_name='profilePicture',
            new_name='profile_picture',
        ),
    ]
