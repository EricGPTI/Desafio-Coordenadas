# Generated by Django 2.2 on 2020-12-21 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201220_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='face',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='x',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='y',
            field=models.IntegerField(null=True),
        ),
    ]