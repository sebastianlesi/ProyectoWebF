# Generated by Django 3.1.6 on 2021-05-21 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('era', '0010_auto_20210521_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
