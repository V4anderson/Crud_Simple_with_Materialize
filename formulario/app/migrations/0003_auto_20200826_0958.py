# Generated by Django 3.1 on 2020-08-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_person_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dt_nasc',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=45, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Primeiro Nome'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Segundo Nome'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=14, verbose_name='Celular'),
        ),
    ]
