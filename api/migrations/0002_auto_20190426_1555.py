# Generated by Django 2.2 on 2019-04-26 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketdata',
            name='nshares',
            field=models.BigIntegerField(default=0),
        ),
    ]
