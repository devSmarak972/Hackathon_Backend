# Generated by Django 4.1.2 on 2022-10-30 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chainbreakers', '0002_rename_quant1_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='buyorder',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sellorder',
            field=models.IntegerField(default=0),
        ),
    ]