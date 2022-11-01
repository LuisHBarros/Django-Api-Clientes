import re
from rest_framework import serializers
from validate_docbr import CPF
cpf = CPF()

def validar_cpf(cpf_number):
    return cpf.validate(cpf_number)
def validar_nome(nome):
    return nome.isalpha()
def validar_rg(rg):
    return len(rg) == 9
def validar_celular(celular):
        model = '[0-9]{2} [0-9]{9}'
        resposta = re.findall(model, celular)
        return resposta
