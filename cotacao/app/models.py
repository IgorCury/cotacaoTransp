from django.db import models

class Cotacao(models.Model):
    cnpjOne=models.CharField(max_length=100)
    nomeEmprOne=models.CharField(max_length=100)
    endOne=models.CharField(max_length=100)
    cnpjTwo=models.CharField(max_length=100)
    nomeEmprTwo=models.CharField(max_length=100)
    endTwo=models.CharField(max_length=100)
    valorNf=models.CharField(max_length=100)
    pesoNf=models.CharField(max_length=100)
    quantNf=models.CharField(max_length=100)
    valorCota=models.CharField(max_length=100)

