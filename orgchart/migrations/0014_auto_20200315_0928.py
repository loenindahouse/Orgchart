# Generated by Django 2.2.11 on 2020-03-15 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgchart', '0013_remove_detail_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='subordinates_url',
        ),
        migrations.AddField(
            model_name='detail',
            name='manager',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
