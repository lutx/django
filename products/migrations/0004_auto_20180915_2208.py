# Generated by Django 2.0.5 on 2018-09-15 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180915_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(default='Twoje posumowanie!!!'),
        ),
    ]
