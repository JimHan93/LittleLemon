# Generated by Django 4.2.5 on 2023-09-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.SmallIntegerField(),
        ),
    ]