# Generated by Django 2.2.5 on 2019-09-28 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='org',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='org',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='career',
            name='period',
            field=models.DateField(auto_now_add=True, verbose_name='Дата начала'),
        ),
    ]