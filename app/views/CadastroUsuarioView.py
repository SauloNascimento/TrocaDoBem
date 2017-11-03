__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"

from django.views.generic import TemplateView


class CadastroUsuarioView(TemplateView):
    template_name = 'cadastros/cadastro-usuario.html'
