# Generated by Django 2.2.5 on 2019-09-28 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0002_auto_20190928_2200'),
        ('education', '0002_auto_20190928_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eduorg',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='eduorg',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='employee',
            name='career',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hunter.Career', verbose_name='Карьера'),
        ),
    ]
