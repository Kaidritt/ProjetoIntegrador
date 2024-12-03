from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes

from .models import Residuo
from .forms import ResiduoForm, CustomUserCreationForm

@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # Use the custom form with the email field
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        # Call the parent method to create the user
        response = super().form_valid(form)
        
        # Retrieve the user instance
        user = self.object

        # Generate a token for email confirmation
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        # Send confirmation email
        mail_subject = 'Activate your account'
        message = render_to_string(
            'registration/account/activation_email.html',
            {
                'user': user,
                'domain': get_current_site(self.request).domain,
                'uid': uid,
                'token': token,
            }
        )
        
        try:
            send_mail(mail_subject, message, 'no-reply@mydomain.com', [user.email])
        except Exception as e:
            # You can log the error or handle it as needed
            messages.error(self.request, "Ocorreu um erro ao enviar o e-mail de confirmação. Tente novamente mais tarde.")
            return redirect('signup')  # Or handle it differently

        # Inform the user that the confirmation email has been sent
        messages.info(self.request, "Um e-mail de confirmação foi enviado para sua conta. Por favor, verifique sua caixa de entrada.")
        
        return response  # Continue with the normal form processing
    
def activate(request, uidb64, token):
    try:
        # Decode UID and get the user
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Check if the token is valid
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True  # Activate the user
        user.save()
        messages.success(request, "Sua conta foi ativada com sucesso!")
        return redirect('login')  # Redirect to login page
    else:
        messages.error(request, "Link de ativação inválido ou expirado.")
        return redirect('home')  # Redirect to home page or any other page

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