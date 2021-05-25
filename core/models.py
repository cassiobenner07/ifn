from django.db import models


class Produto (models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.DecimalField('Quantidade em estoque', decimal_places=2, max_digits=8)

    def __str__(self):
        return f' {self.nome}, {self.estoque}'


class Cliente (models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.nome},{self.sobrenome}'