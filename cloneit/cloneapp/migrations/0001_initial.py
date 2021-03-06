# Generated by Django 3.0.6 on 2020-07-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('laptop', 'laptop'), ('mobile', 'mobile'), ('headphone', 'headphone'), ('speakers', 'speakers')], default='laptop', max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('price', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
        ),
    ]
