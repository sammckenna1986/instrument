# Generated by Django 3.1.4 on 2020-12-08 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]