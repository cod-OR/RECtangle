# Generated by Django 3.1.13 on 2021-08-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210818_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='coordinator1',
            field=models.CharField(choices=[('onkar', 'onkar')], default='A', max_length=10),
        ),
        migrations.AlterField(
            model_name='problem',
            name='coordinator2',
            field=models.CharField(choices=[('onkar', 'onkar')], default='A', max_length=10),
        ),
    ]
