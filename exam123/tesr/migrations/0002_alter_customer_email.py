# Generated by Django 4.1.6 on 2023-02-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
