from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        # Chama o método pai e armazena a resposta
        response = super().form_valid(form)
        # Adiciona mensagem de sucesso após o cadastro
        messages.success(self.request, "Usuário cadastrado com sucesso.")
        return response

    def form_invalid(self, form):
        # Verifica se o erro de usuário já existente está presente
        if 'username' in form.errors:
            username_error = form.errors['username']
            if "A user with that username already exists." in username_error:
                messages.error(self.request, "Nome de usuário já cadastrado!")

        # Verifica se o erro de senhas não conferem está presente
        if 'password2' in form.errors:
            password_error = form.errors['password2']
            if "The two password fields didn’t match." in password_error:
                messages.error(self.request, "Senhas não conferem.")

        # Verifica se o erro de senha similar ao nome de usuário está presente
        if 'password1' in form.errors:
            password1_error = form.errors['password1']
            if "This password is too similar to the username." in password1_error:
                messages.error(self.request, "A senha é muito similar ao nome de usuário.")

        # Chama o método pai para retornar a resposta apropriada
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

def tipos_de_residuo(request):
    # Your logic here
    residuos = ['Metal', 'Papel', 'Plástico']
    return render(request, 'tipos-de-residuo.html', {'residuos': residuos})

def pontos_de_coleta(request):
    # Your logic here
    return render(request, 'pontos-de-coleta.html')