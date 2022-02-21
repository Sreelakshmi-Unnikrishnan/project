# Generated by Django 3.0.7 on 2022-02-21 09:43

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.ImageField(upload_to='', validators=[app.validators.validate_image], verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='video',
            field=models.FileField(upload_to='', validators=[app.validators.validate_video], verbose_name='video'),
        ),
    ]