# Generated by Django 2.2 on 2020-12-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='x',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='position',
            name='y',
            field=models.IntegerField(),
        ),
    ]