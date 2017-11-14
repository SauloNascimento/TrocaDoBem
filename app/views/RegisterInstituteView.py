from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from app.models import Institute

__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"


class CadastroInstituicaoView(TemplateView):
    template_name = 'registers/register-institute.html'


def cadastro_inst(request):
    inst = Institute(cnpj=request.POST['CNPJ'], senha=request.POST['senha'],
                     name=request.POST['nome'],
                     cep=request.POST['cep'], estado=request.POST['estado'], cidade=request.POST['cidade'],
                     bairro=request.POST['bairro'], rua=request.POST['rua'], numero=request.POST['numero'],
                     complemento=request.POST['complemento'], email=request.POST['email'],
                     telefone=request.POST['telefone'])
    try:
        inst.save()
        messages.success(request, 'Nova instituição cadastrada com sucesso.')
    except:
        messages.error(request, 'Instituição não foi cadastrada.')

    return HttpResponseRedirect(reverse('home'))
