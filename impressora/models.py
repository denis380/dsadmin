from django.db import models
from django import forms

class Printer(models.Model):
    serial = models.CharField(max_length=20, primary_key=True)
    ip = models.GenericIPAddressField(null=True)
    modelo = models.CharField(max_length=8, null=True)
    contador = models.IntegerField(null=True)
    etiqueta = models.CharField(max_length=15)
    galpao = models.CharField(max_length=4)
    coluna = models.CharField(max_length=20)
    status = models.CharField(max_length=30, null=True)


    def __str__(self): # Exibe as impressoras pelo serial no banco de dados pelo django Admin.
        return self.serial

    def save(self, force_insert=False, force_update=False):# Função para salvar os campos em maiúsculo.
        self.serial = self.serial.upper()
        self.etiqueta = self.etiqueta.upper()
        self.modelo = self.modelo.upper()
        self.galpao = self.galpao.upper()
        self.coluna = self.coluna.upper()

        super(Printer, self).save(force_insert, force_update)


