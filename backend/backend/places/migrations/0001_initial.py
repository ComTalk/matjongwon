# Generated by Django 4.1.3 on 2023-05-23 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('category', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('opening_hours', models.TextField(blank=True, null=True)),
                ('score_navermap', models.TextField(blank=True, db_column='score.navermap', null=True)),
                ('score_kakaomap', models.TextField(blank=True, db_column='score.kakaomap', null=True)),
                ('score_googlemap', models.TextField(blank=True, db_column='score.googlemap', null=True)),
                ('menu', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('reviews_navermap', models.TextField(blank=True, db_column='reviews.navermap', null=True)),
                ('reviews_kakaomap', models.TextField(blank=True, db_column='reviews.kakaomap', null=True)),
                ('reviews_googlemap', models.TextField(blank=True, db_column='reviews.googlemap', null=True)),
                ('thumbnails', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('coordinates_latitude', models.FloatField(db_column='coordinates.latitude')),
                ('coordinates_longitude', models.FloatField(db_column='coordinates.longitude')),
            ],
            options={
                'db_table': 'seoul',
                'managed': False,
            },
        ),
    ]
