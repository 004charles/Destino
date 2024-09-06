from django.urls import path
from . import views
from .views import (
    RegisterAPIView,
    LoginAPIView,
    ViagensListAPIView,
    BilheteAPIView,
    PagamentoAPIView,
    EstacoesPorProvinciaAPIView,
    ViagemDetailAPIView
)


urlpatterns = [
    path('index/', views.index, name = "index"),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('viagens/', ViagensListAPIView.as_view(), name='viagens_list'),
    path('bilhete/', BilheteAPIView.as_view(), name='bilhete_create'),
    path('pagamento/', PagamentoAPIView.as_view(), name='pagamento_create'),
    path('estacoes/', EstacoesPorProvinciaAPIView.as_view(), name='estacoes_por_provincia'),
    path('viagem/<int:pk>/', ViagemDetailAPIView.as_view(), name='viagem_detail'),
]
