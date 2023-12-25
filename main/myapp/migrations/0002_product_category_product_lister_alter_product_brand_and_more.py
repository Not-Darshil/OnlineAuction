# Generated by Django 5.0 on 2023-12-24 16:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='lister',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=512, null=True),
        ),
    ]