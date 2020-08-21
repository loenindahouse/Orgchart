# Generated by Django 2.2.11 on 2020-03-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgchart', '0009_auto_20200314_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='department',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='detail',
            name='last_name',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AlterField(
            model_name='detail',
            name='location',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='personal_email',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='detail',
            name='preferred_name',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AlterField(
            model_name='detail',
            name='status',
            field=models.CharField(default='Deactive', max_length=10),
        ),
        migrations.AlterField(
            model_name='detail',
            name='subordinates_url',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='work_phone',
            field=models.TextField(default='None'),
        ),
    ]
