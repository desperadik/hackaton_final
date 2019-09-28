# Generated by Django 2.2.5 on 2019-09-28 22:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190928_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstracttypedir',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='abstracttypedir',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
