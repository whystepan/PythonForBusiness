# Generated by Django 4.0.4 on 2022-05-26 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursach', '0003_tourpetition_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Название тура'),
        ),
        migrations.AlterField(
            model_name='tourpetition',
            name='phone',
            field=models.CharField(max_length=32, verbose_name='Номер телефона'),
        ),
    ]