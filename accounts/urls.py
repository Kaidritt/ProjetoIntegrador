from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, ResiduoCreateView, ResiduoDetailView, tipos_residuo, pontos_coleta

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('residuo/<int:pk>/', ResiduoDetailView.as_view(), name='residuo-detalhe'),
    path('tipos-de-residuo/', tipos_residuo, name='tipos_residuo'),
    path('criar-residuo/', ResiduoCreateView.as_view(), name='criar-residuo'),
    path('pontos-de-coleta/', pontos_coleta, name='pontos_coleta'),
     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]