# Generated by Django 3.2.9 on 2022-02-12 18:30

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='image',
            field=models.ImageField(null=True, upload_to=music.models.upload_to),
        ),
        migrations.AlterField(
            model_name='songs',
            name='music',
            field=models.FileField(null=True, upload_to=music.models.upload_to),
        ),
    ]
