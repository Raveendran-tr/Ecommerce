# Generated by Django 4.1.7 on 2023-03-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
