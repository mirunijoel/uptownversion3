# Generated by Django 3.0.7 on 2020-06-19 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200619_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='product_type',
        ),
    ]
