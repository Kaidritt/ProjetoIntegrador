from django.urls import path
from .views import SignUpView, ResiduoCreateView, ResiduoDetailView, tipos_residuo, pontos_coleta

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('residuo/<int:pk>/', ResiduoDetailView.as_view(), name='residuo_detalhe'),
    path('tipos-de-residuo/', tipos_residuo, name='tipos_residuo'),
    path('criar-residuo/', ResiduoCreateView.as_view(), name='criar_residuo'),
    path('pontos-de-coleta/', pontos_coleta, name='pontos_coleta'),
]