#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from app.models import Requirement, Item
from app.models import Post, Message, Institute
from app.forms import FormRequirement
from django.template import RequestContext

"""HomeView.py: Especifica a pagina inicial da aplicacao."""

__author__ = "Alberto Wagner"
__copyright__ = "Copyright 2017, LES-UFCG"


class HomeView(ListView):
    def get(self, request, *args, **kwargs):
        requeriments = Requirement.objects.all()
        queryset = Post.objects.filter(is_visible=True).order_by('-created_at')[:6]
        itens = Item.objects.all().filter(status=True)
        form = FormRequirement
        return render(request, 'index.html', {'requeriments': requeriments,
                                              'form': form, 'recent_posts': queryset, 'itens': itens})


class CollectView(TemplateView):
    template_name = 'collect.html'


class ContributeView(TemplateView):
    template_name = 'contribute.html'


class InstitutesView(ListView):
    template_name = 'institutes.html'
    model = Institute
    context_object_name = 'institutes'
    queryset = Institute.objects.all().order_by('-created_at')[:6]


def submit_message(request):
    data = request.POST
    name = data.get('name')
    message = data.get('message')
    email = data.get('email')
    try:
        objeto = Message(name=name, email=email, message=message)
        objeto.save()
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('/')
    except Exception:
        messages.error(request, 'Houve algum erro.')
        return redirect('/')


def view_post(request, slug):
    return render_to_response('post.html', {'post': get_object_or_404(Post, slug=slug)},
                              context_instance=RequestContext(request))
