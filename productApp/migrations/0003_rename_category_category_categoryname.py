# Generated by Django 4.0.2 on 2022-03-26 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0002_remove_products_productimage_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category',
            new_name='CategoryName',
        ),
    ]