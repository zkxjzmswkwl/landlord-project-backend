# Generated by Django 4.0.3 on 2022-03-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='reyzrs_mom',
            field=models.BooleanField(default=False),
        ),
    ]
