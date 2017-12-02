#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView, TemplateView

from app.models import Post, Message, Institute

"""HomeView.py: Especifica a pagina inicial da aplicacao."""

__author__ = "Alberto Wagner"
__copyright__ = "Copyright 2017, LES-UFCG"


class HomeView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'recent_posts'
    queryset = Post.objects.filter(is_visible=True).order_by('-created_at')[:6]



class collectView(TemplateView):
    template_name = 'collect.html'

class contributeView(TemplateView):
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
