# Generated by Django 2.0.4 on 2018-06-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServerApp', '0006_auto_20180613_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]