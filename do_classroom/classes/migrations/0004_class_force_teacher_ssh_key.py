# Generated by Django 2.2.10 on 2020-04-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_remove_class_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='force_teacher_ssh_key',
            field=models.BooleanField(default=False),
        ),
    ]
