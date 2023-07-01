# Generated by Django 4.2.2 on 2023-06-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authormodel',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='authormodel',
            name='lastname',
        ),
        migrations.AddField(
            model_name='authormodel',
            name='name',
            field=models.CharField(default='Not Given', max_length=100),
        ),
        migrations.AlterModelTable(
            name='bookmodel',
            table='book',
        ),
    ]
