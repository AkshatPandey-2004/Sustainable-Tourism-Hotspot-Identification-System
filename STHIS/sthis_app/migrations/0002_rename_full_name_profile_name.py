# Generated by Django 4.2.7 on 2024-03-16 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sthis_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='full_name',
            new_name='Name',
        ),
    ]