# Generated by Django 4.0.4 on 2022-05-26 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursach', '0002_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourpetition',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursach.tour'),
        ),
    ]
