from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self,data):
        if not validar_nome(data['nome']):
            raise serializers.ValidationError({'nome':"O nome nao pode conter caracteres numéricos"})
        if not validar_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF invalido. (apenas números)"})
        if not validar_rg(data['rg']):
            raise serializers.ValidationError({'rg': "O rg deve ter 9 dígitos."})
        if not validar_celular(data['celular']):
            raise serializers.ValidationError({'celular': "número de celular invalido. Siga esse modelo 'xx xxxxxxxxx'"})
        return data
