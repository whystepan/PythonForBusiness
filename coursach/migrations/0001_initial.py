# Generated by Django 4.0.4 on 2022-05-26 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourPetition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=20, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('date', models.DateField(verbose_name='Дата проведения')),
                ('persons_count', models.IntegerField(default=1, verbose_name='Количество персон')),
            ],
        ),
    ]
