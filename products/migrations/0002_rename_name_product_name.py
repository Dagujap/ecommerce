# Generated by Django 5.0.1 on 2024-02-02 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_migrate_products_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Name',
            new_name='name',
        ),
    ]
