from django.views.generic import TemplateView
from app.models import Instituicao
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"


class CadastroInstituicaoView(TemplateView):
    template_name = 'cadastros/cadastro-instituicao.html'

def cadastroInst(request):
    inst = Instituicao(photo=request.POST['photo'], cnpj=request.POST['cnpj'], name=request.POST['name'], cep=request.POST['photo'], estado=request.POST['estado'], cidade=request.POST['cidade'], bairro=request.POST['bairro'], rua=request.POST['rua'], numero=request.POST['numero'], complemento=request.POST['complemento'], descricao=request.POST['descricao'], email=request.POST['email'], telefone=request.POST['telefone'])
    inst.save()
    return HttpResponseRedirect(reverse('home', args=()))