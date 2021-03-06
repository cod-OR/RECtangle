# Generated by Django 3.1.13 on 2022-01-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220108_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='coordinator1',
            field=models.CharField(choices=[('onkar', 'onkar'), ('onkar2', 'onkar2'), ('onkar232323', 'onkar232323')], default='A', max_length=20),
        ),
        migrations.AlterField(
            model_name='problem',
            name='coordinator2',
            field=models.CharField(choices=[('onkar', 'onkar'), ('onkar2', 'onkar2'), ('onkar232323', 'onkar232323')], default='A', max_length=20),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')], default='A', max_length=30),
        ),
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(choices=[('Queued', 'Queued'), ('Rejected', 'Rejected'), ('Testing', 'Testing'), ('Done', 'Done')], default='Queued', max_length=30),
        ),
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
