# Generated by Django 4.1.3 on 2023-05-23 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('_id', models.CharField(max_length=24, primary_key=True, serialize=False)),
            ],
        ),
    ]