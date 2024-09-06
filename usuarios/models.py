from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=12)
    senha = models.CharField(max_length=100)
    data_criacao = models.DateField()

    def __str__(self) -> str:
        return self.nome
    
class Provincias(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20)

    def __str__(self) -> str:
     return self.nome
    
class Estacoes(models.Model):
   nome = models.CharField(max_length=50)
   provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
   endereco = models.CharField(max_length=100)

   def __str__(self) -> str:
     return self.nome
    
class Autocarros(models.Model):
   placa = models.CharField(max_length=50)
   modelo = models.CharField(max_length=50)
   capacidade = models.IntegerField()

   
class Viagens(models.Model):
    autocarro = models.ForeignKey(Autocarros, on_delete=models.CASCADE)
    origem = models.ForeignKey(Estacoes, on_delete=models.CASCADE, related_name='viagens_origem')
    destino = models.ForeignKey(Estacoes, on_delete=models.CASCADE, related_name='viagens_destino')
    data_partida = models.DateField()
    hora = models.CharField(max_length=6)
    preco = models.FloatField()
    lugar_disponivel = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.origem} para {self.destino} em {self.data_partida}"

class Bilhete(models.Model):
   usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
   viagem = models.ForeignKey(Viagens, on_delete=models.CASCADE)
   data_compra = models.DateField(auto_now_add=True)
   codigo_bilhete = models.CharField(max_length=20)
   
class Pagamento(models.Model):
   usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
   bilhete = models.ForeignKey(Bilhete, on_delete=models.CASCADE)
   metodo_pagamento = models.CharField(max_length=100)
   status_pagamento = models.CharField(max_length=100)
   data_pagamento = models.DateField()

   
class Api(models.Model):
   nome = models.CharField(max_length=100)
   url = models.URLField()
    
   def __str__(self) -> str:
     return self.nome



