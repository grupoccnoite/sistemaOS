# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('clientes', '0004_remove_cliente_os'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ManyToManyField(to='enderecos.Endereco'),
        ),
    ]
