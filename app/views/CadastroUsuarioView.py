from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from app.models import Usuario

__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"


class CadastroUsuarioView(TemplateView):
    template_name = 'cadastros/cadastro-usuario.html'


def cadastro_usuario(request):
    user = Usuario(
        nome=request.POST['nome'],
        cpf=request.POST['cpf'],
        dataNascimento=request.POST['dataNascimento'],
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
        messages.success(request, 'Novo usuário cadastrado com sucesso.')
    except:
        messages.error(request, 'Usuário não foi cadastrado.')
    return HttpResponseRedirect(reverse('home'))
