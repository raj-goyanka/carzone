# Generated by Django 4.0.1 on 2022-01-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='milage',
            field=models.IntegerField(),
        ),
    ]