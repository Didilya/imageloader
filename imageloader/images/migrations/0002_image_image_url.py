# Generated by Django 3.1.7 on 2021-02-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
