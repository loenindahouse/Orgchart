# Generated by Django 2.2.11 on 2020-03-16 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgchart', '0016_auto_20200316_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]