# Generated by Django 3.0.1 on 2022-06-24 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notesapp', '0003_auto_20220623_0915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together={('user', 'title')},
        ),
    ]
