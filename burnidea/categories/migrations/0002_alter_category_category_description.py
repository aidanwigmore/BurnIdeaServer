# Generated by Django 5.1.3 on 2025-01-19 00:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
