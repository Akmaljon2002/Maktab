# Generated by Django 4.2.1 on 2023-05-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0005_remove_oqituvchi_fan_oqituvchi_fan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oqituvchi',
            name='fan',
        ),
        migrations.AddField(
            model_name='fanlar',
            name='oqituvchi',
            field=models.ManyToManyField(to='asosiy.oqituvchi'),
        ),
    ]
