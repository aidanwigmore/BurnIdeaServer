# Generated by Django 5.1.3 on 2025-01-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('visible', models.BooleanField(default=True)),
                ('category_description', models.TextField()),
                ('color', models.CharField(default='black', max_length=100)),
                ('ideas', models.ManyToManyField(related_name='ideas', to='ideas.idea')),
            ],
        ),
    ]