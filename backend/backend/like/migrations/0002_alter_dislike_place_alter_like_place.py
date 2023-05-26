# Generated by Django 4.1.3 on 2023-05-23 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='place',
            field=models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='places.place'),
        ),
        migrations.AlterField(
            model_name='like',
            name='place',
            field=models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='places.place'),
        ),
    ]
