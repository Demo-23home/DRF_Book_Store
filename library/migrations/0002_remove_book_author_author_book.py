# Generated by Django 4.2.7 on 2023-11-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(to='library.book'),
        ),
    ]
