# Generated by Django 4.1.7 on 2023-04-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(upload_to='pets'),
        ),
    ]
