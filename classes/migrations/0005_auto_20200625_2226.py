# Generated by Django 3.0.7 on 2020-06-25 22:26

import classes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_class_force_teacher_ssh_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='prefix',
            field=models.CharField(default=classes.models.prefix_generator, max_length=15, unique=True),
        ),
    ]
