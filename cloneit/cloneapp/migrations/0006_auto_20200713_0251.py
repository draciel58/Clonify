# Generated by Django 3.0.8 on 2020-07-13 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloneapp', '0005_auto_20200711_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product',
            field=models.CharField(choices=[('laptop', 'laptop'), ('mobile', 'mobile'), ('headphone', 'headphone'), ('speakers', 'speakers'), ('keyboard', 'keyboard')], default='laptop', max_length=20),
        ),
    ]
