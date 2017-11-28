"""urls.py: Urls definidas."""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.views.HomeView import HomeView, submit_message, view_post
from app.views.LoginView import LoginView, LogoutView
from app.views.PainelInstituteView import PainelInstituteView
from app.views.RegisterInstituteView import RegisterInstituteView
from app.views.ObjectView import RegisterObjectView, ObjectView, MyDonationsListView, ObjectUpdateView
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
    url(r'^register-institute/$', RegisterInstituteView.as_view(), name='register_institute'),
    url(r'^register-user/$', RegisterUserView.as_view(), name='register_user'),
    url(r'^submit-contact', submit_message, name='submit_contact'),
    url(r'^post/(?P<slug>[^\.]+)', view_post, name='view_post'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^account/logout/$', LogoutView.as_view(), name='auth_logout'),
    url(r'^home/$', PainelInstituteView.as_view(), name='painel'),
    url(r'^object/add/$', RegisterObjectView.as_view(), name='add_object'),
    url(r'^object/(?P<pk>[0-9]+)/$', ObjectView.as_view(), name='view-object'),
    url(r'^donations/$', MyDonationsListView.as_view(), name='list_my_donations'),
    url(r'^object/(?P<pk>[0-9]+)/edit/$', ObjectUpdateView.as_view(), name='change_object')
]
