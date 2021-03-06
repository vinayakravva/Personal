# Generated by Django 3.2.5 on 2021-08-11 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='courses',
            name='updated_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
