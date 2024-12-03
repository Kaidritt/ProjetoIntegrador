from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView
from django.contrib import messages
from django.utils.decorators import method_decorator
from .models import Residuo
from .forms import ResiduoForm, CustomUserCreationForm


@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # Use the custom form with the email field
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        # Call the parent method and store the response
        response = super().form_valid(form)
        # Add success message after registration
        messages.success(self.request, "Usuário cadastrado com sucesso.")
        
        # Limpa a fila de mensagens de erro após o sucesso
        if '_messages' in self.request.session:
            del self.request.session['_messages']
    
        return response

    def form_invalid(self, form):
        # Check for errors specific to username, password, and email
        if 'username' in form.errors:
            username_error = form.errors['username']
            if "A user with that username already exists." in username_error:
                messages.error(self.request, "Nome de usuário já cadastrado!")

        if 'password2' in form.errors:
            password_error = form.errors['password2']
            if "The two password fields didn’t match." in password_error:
                messages.error(self.request, "Senhas não conferem.")

        if 'password1' in form.errors:
            password1_error = form.errors['password1']
            if "This password is too similar to the username." in password1_error:
                messages.error(self.request, "A senha é muito similar ao nome de usuário.")
        
        # Check for email errors, e.g., invalid email format or email already in use
        if 'email' in form.errors:
            email_error = form.errors['email']
            if "Enter a valid email address." in email_error:
                messages.error(self.request, "Por favor, insira um e-mail válido.")
            elif "This field must be unique." in email_error:
                messages.error(self.request, "Este e-mail já está em uso.")

        # Call the parent method to return the appropriate response
        return super().form_invalid(form)

#@csrf_exempt  # Use isso apenas para desenvolvimento; em produção, use CSRF corretamente
#class SubscribeView(View):
#    def post(self, request):
#        email = request.POST.get('email')
#        if email:
#            try:
#               subscription = Subscription(email=email)
#               subscription.save()
#                return JsonResponse({'message': 'Inscrição realizada com sucesso!'}, status=201)
#            except Exception as e:
#                return JsonResponse({'error': str(e)}, status=400)
#        return JsonResponse({'error': 'Email não fornecido.'}, status=400)

class ResiduoCreateView(UserPassesTestMixin, CreateView):
    model = Residuo
    form_class = ResiduoForm
    template_name = 'criar-residuo.html'

    def get_success_url(self):
        return reverse_lazy('residuo-detalhe', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Custom validation for duplicate tipoResiduo
        tipo_residuo = form.cleaned_data['tipoResiduo']
        if Residuo.objects.filter(tipoResiduo=tipo_residuo).exists():
            form.add_error('tipoResiduo', f'O resíduo "{tipo_residuo}" já foi cadastrado!')
            return self.form_invalid(form)

        response = super().form_valid(form)
        messages.success(self.request, f"Resíduo '{self.object.tipoResiduo}' cadastrado com sucesso!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar tipo de resíduo!")
        return super().form_invalid(form)

    def test_func(self):
        # Restrict access to admins only
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return redirect('home')

class ResiduoDetailView(DetailView):
    model = Residuo
    template_name = 'residuo-detalhe.html'
    context_object_name = 'residuo'

def tipos_residuo(request):
    search_term = request.GET.get('search', '')
    residuos = Residuo.objects.filter(tipoResiduo__icontains=search_term) if search_term else Residuo.objects.all()
    
    return render(request, 'tipos-de-residuo.html', {'residuos': residuos, 'search_term': search_term})

def pontos_coleta(request):
    return render(request, 'pontos-de-coleta.html')