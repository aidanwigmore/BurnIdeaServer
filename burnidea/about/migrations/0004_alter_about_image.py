# Generated by Django 5.1.3 on 2025-01-29 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_about_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='about/'),
        ),
    ]
