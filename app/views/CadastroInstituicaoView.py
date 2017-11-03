__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"

from django.views.generic import TemplateView

class CadastroInstituicaoView(TemplateView):
    template_name = 'cadastros/cadastro-instituicao.html'