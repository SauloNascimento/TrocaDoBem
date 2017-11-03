"""HomeView.py: Especifica a pagina inicial da aplicacao."""

__author__ = "Alberto Wagner"
__copyright__ = "Copyright 2017, LES-UFCG"

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

