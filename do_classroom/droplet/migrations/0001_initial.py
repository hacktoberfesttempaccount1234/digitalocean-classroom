# Generated by Django 2.2.7 on 2019-12-17 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Droplet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('droplet_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=64)),
                ('image', models.CharField(max_length=64)),
                ('ip_addr', models.GenericIPAddressField()),
                ('initial_password', models.CharField(max_length=512)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classes.Class')),
            ],
        ),
    ]
