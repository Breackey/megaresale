# Generated by Django 2.2 on 2019-04-16 05:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190416_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
