# Generated by Django 3.0.5 on 2020-10-11 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_auto_20201010_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clp',
            name='fin_vigencia',
            field=models.DateField(blank=True, null=True, verbose_name='Fin vigencia'),
        ),
        migrations.AlterField(
            model_name='clp',
            name='inicio_vigencia',
            field=models.DateField(blank=True, null=True, verbose_name='Inicio vigencia'),
        ),
        migrations.AlterField(
            model_name='clp',
            name='representante_proyecto',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Representante del proyecto'),
        ),
    ]