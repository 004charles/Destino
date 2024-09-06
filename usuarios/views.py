from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


from django.db.models import Q
from .models import Usuarios, Viagens, Estacoes, Bilhete, Autocarros, Provincias, Pagamento, Api
from .serializers import (
    UsuariosSerializer, 
    ViagemSerializer, 
    EstacoesSerializer, 
    BilheteSerializer, 
    AutocarroSerializer, 
    ProvinciasSerializer, 
    PagamentoSerializer
)

# Cadastro de usuários
class RegisterAPIView(generics.CreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

# Login de usuários
class LoginAPIView(generics.GenericAPIView):
    serializer_class = UsuariosSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        senha = request.data.get('senha')
        user = authenticate(email=email, password=senha)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# Pesquisa de viagens
class ViagensListAPIView(generics.ListAPIView):
    serializer_class = ViagemSerializer

    def get_queryset(self):
        origem = self.request.query_params.get('origem')
        destino = self.request.query_params.get('destino')
        return Viagens.objects.filter(
            Q(origem__nome=origem) & Q(destino__nome=destino)
        )

# Compra de bilhete
class BilheteAPIView(generics.CreateAPIView):
    serializer_class = BilheteSerializer

    def post(self, request, *args, **kwargs):
        # Aqui você pode adicionar lógica para verificar disponibilidade e outras regras
        return super().post(request, *args, **kwargs)

# Confirmar pagamento
class PagamentoAPIView(generics.CreateAPIView):
    serializer_class = PagamentoSerializer

# Listar estações por província
class EstacoesPorProvinciaAPIView(generics.ListAPIView):
    serializer_class = EstacoesSerializer

    def get_queryset(self):
        provincia_id = self.request.query_params.get('provincia')
        return Estacoes.objects.filter(provincia__id=provincia_id)

# Detalhes da viagem
class ViagemDetailAPIView(generics.RetrieveAPIView):
    queryset = Viagens.objects.all()
    serializer_class = ViagemSerializer

def index(request):
    api = Api.objects.all
    return render(request, 'index.html', {'api': api})
