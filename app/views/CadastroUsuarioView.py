from django.views.generic import TemplateView
from app.models import Usuario
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"


class CadastroUsuarioView(TemplateView):
    template_name = 'cadastros/cadastro-usuario.html'


def cadastro_usuario(request):
    user = Usuario(
                   nome=request.POST['nome'],
                   cpf=request.POST['cpf'],
                   dataNascimento=request.POST['data de nascimento'],
                   cep=request.POST['cep'],
                   estado=request.POST['estado'],
                   cidade=request.POST['cidade'],
                   bairro=request.POST['bairro'],
                   rua=request.POST['rua'],
                   numero=request.POST['numero'],
                   complemento=request.POST['complemento'],
                   telefone=request.POST['telefone'],
                   email=request.POST['email'],
                   senha=request.POST['senha'],
                   login=request.POST['login'],
                   )
    try:
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso.')
    except:
        messages.error(request, 'Cadastro não realizado.')
    return HttpResponseRedirect(reverse('home', args=()))
