# Generated by Django 4.0.6 on 2022-10-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
