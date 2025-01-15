# Generated by Django 5.1.3 on 2025-01-15 21:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_alter_idea_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]