from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuarios, Viagens, Estacoes, Bilhete, Autocarros, Provincias, Pagamento

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

        def validate_email(self, value):
            if Usuarios.objects.filter(email=value).exists():
                raise serializers.ValidationError("Este e-mail já está em uso.")
            return value

        def create(self, validated_data):
            senha = validated_data.pop('senha', None)
            usuario = Usuarios.objects.create(**validated_data)
            if senha:
                usuario.senha = make_password(senha)
                usuario.save()
            return usuario

class ViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viagens
        fields = '__all__'

class EstacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacoes
        fields = '__all__'

class BilheteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bilhete
        fields = '__all__'

class AutocarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autocarros
        fields = '__all__'

class ProvinciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincias
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'
