from django.views.generic import TemplateView
from app.models import Usuario
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"


class CadastroUsuarioView(TemplateView):
    template_name = 'cadastros/cadastro-usuario.html'


def cadastroUsuario(request):
    usuario = Usuario(photo=request.POST['photo'], nome=request.POST['nome'],
                      dataNascimento=request.POST['data de nascimento'], cpf=request.POST['cpf'],
                      email=request.POST['email'], endereco=request.POST['endereco'],
                      numero=request.POST['numero'], bairro=request.POST['bairro'], cep=request.POST['cep'],
                      complemento=request.POST['complemento'], cidade=request.POST['cidade'],
                      estado=request.POST['estado'], telefone=request.POST['telefone'])

    usuario.save()
    return HttpResponseRedirect(reverse('home', args=()))
