# Generated by Django 2.2.11 on 2020-03-13 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgchart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='department',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='employments',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='location',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='subordinates',
        ),
    ]
