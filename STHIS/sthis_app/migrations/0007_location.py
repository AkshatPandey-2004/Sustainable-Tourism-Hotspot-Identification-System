# Generated by Django 4.2.7 on 2024-03-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sthis_app', '0006_rename_p_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('add', models.CharField(max_length=200)),
                ('acti', models.CharField(max_length=1000)),
                ('culture', models.CharField(max_length=100000)),
            ],
        ),
    ]