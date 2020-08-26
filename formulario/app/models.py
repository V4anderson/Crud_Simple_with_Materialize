from django.db import models

class Person(models.Model):
    first_name = models.CharField('Primeiro Nome',max_length=30)
    last_name = models.CharField('Segundo Nome',max_length=30)
    phone = models.CharField('Celular',max_length=14)
    email = models.CharField('Email',max_length=45)
    dt_nasc = models.DateField('Data de Nascimento',auto_now=False)