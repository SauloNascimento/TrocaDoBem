from django.views.generic import TemplateView

__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"


class CadastroUsuarioView(TemplateView):
    template_name = 'cadastros/cadastro-usuario.html'
