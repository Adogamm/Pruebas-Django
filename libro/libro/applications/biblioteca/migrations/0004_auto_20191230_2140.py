# Generated by Django 3.0.1 on 2019-12-30 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_auto_20191230_2139'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Libros',
            new_name='Libro',
        ),
    ]