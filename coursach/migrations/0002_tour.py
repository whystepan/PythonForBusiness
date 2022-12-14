# Generated by Django 4.0.4 on 2022-05-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursach', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Название тура')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='static', verbose_name='Фото')),
            ],
        ),
    ]
