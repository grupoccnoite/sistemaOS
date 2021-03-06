from django.db import models
from auditlog.registry import auditlog

# Create your models here.

class InfoAbst(models.Model):
        nome = models.CharField(max_length = 100)
        telefone = models.CharField(max_length=15, help_text='Seguir o formato como exemplo: 83-11111-2222')
	email = models.EmailField(max_length = 70)

class Meta:
	abstract = True

class Cliente(InfoAbst):
       cpf = models.PositiveIntegerField(max_length = 11, blank = True, null = True, help_text='Digitar apenas numeros', unique = True)
       cnpj = models.PositiveIntegerField(max_length = 14, blank = True, null = True, help_text='Digitar apenas numeros', unique = True)
       endereco = models.ManyToManyField('enderecos.Endereco')
       num = models.PositiveIntegerField(blank = True, null = True)	
       
       def __unicode__(self):
         return self.nome

auditlog.register(Cliente)

