# Generated by Django 4.1.5 on 2023-01-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-year']},
        ),
        migrations.AlterField(
            model_name='inventory',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
