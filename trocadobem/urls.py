"""urls.py: Urls definidas."""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.views.HomeView import HomeView, submit_message, view_post
from app.views.RegisterUserView import RegisterUserView

__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"

"""default URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/login/$', auth_views.login),
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^register-institute/$', CadastroInstituicaoView.as_view(), name='register_institute'),
    # url(r'^cadastrar-instituicao/cadastro_inst_proc', cadastro_inst, name='cadastro_inst_proc'),
    url(r'^register-user/$', RegisterUserView.as_view(), name='register_user'),
    # url(r'^cadastrar-usuario/cadastro_usuario_proc', cadastro_usuario, name='cadastro_usuario_proc'),
    url(r'^submit-contact', submit_message, name='submit_contact'),
    url(r'^post/(?P<slug>[^\.]+)', view_post, name='view_post'),
]
