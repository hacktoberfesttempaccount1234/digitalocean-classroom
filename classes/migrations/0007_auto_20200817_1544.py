# Generated by Django 3.0.7 on 2020-08-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_class_allow_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='droplet_count',
            field=models.IntegerField(default=0),
        ),
    ]