# Generated by Django 5.1.3 on 2025-01-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=models.TextField(),
        ),
    ]
