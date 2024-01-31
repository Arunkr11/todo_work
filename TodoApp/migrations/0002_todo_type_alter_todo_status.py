# Generated by Django 5.0.1 on 2024-01-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='type',
            field=models.CharField(choices=[('pending', 'pending'), ('complete', 'complete'), ('in-progress', 'in-progress')], default='pending', max_length=225),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(max_length=225),
        ),
    ]