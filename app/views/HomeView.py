from django.views.generic import TemplateView

"""HomeView.py: Especifica a pagina inicial da aplicacao."""

__author__ = "Alberto Wagner"
__copyright__ = "Copyright 2017, LES-UFCG"


class HomeView(TemplateView):
    template_name = 'cadastros/doacaoanonima.html'
