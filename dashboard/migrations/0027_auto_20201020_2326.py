# Generated by Django 3.0.5 on 2020-10-21 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_auto_20201020_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cxc',
            name='oef_asignada',
            field=models.IntegerField(verbose_name='OEF asignada'),
        ),
    ]