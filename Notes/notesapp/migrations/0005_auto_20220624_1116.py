# Generated by Django 3.0.1 on 2022-06-24 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0004_auto_20220624_0416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ('created_at',)},
        ),
    ]
