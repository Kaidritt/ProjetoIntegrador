from django.urls import path
from .views import SignUpView, tipos_de_residuo, pontos_de_coleta

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('tipos-de-residuo/', tipos_de_residuo, name='tipos_de_residuo'),
    path('pontos-de-coleta/', pontos_de_coleta, name='pontos_de_coleta'),
]