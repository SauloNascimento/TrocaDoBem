"""urls.py: Urls definidas."""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.views.AuditView import AuditListView, order_item, \
    AuditAllListView, AuditDetailView, AuditUpdateView, \
    delete_audit, HomeAuditView, AuditUserListView, \
    accept_audit, refuse_audit, final_delivery, refuse_delivery
from app.views.DonationView import DonationListView, DonationUpdateView, \
    delete_donation, ChooseDonation, \
    AnonDonationFormView
from app.views.DonatorUpdateView import DonatorUpdateView
from app.views.HomeView import HomeView, submit_message, view_post, InstitutesView, \
    CollectView, ContributeView
from app.views.InstituteUpdateView import InstituteUpdateView
from app.views.LoginView import LoginView, LogoutView
from app.views.MatchView import MatchListView, MatchUpdateView, delete_match
from app.views.NotificationView import NotificationListView, accept_notification, \
    refuse_notification
from app.views.ObjectView import RegisterObjectView, ObjectView, MyDonationsListView, MyItensListView, \
    ObjectUpdateView, delete_object
from app.views.OrderView import OrderUpdateView
from app.views.OrderView import delete_order, OrderListView
from app.views.PainelView import PainelView, ProfileUserView
from app.views.RegisterInstituteView import RegisterInstituteView
from app.views.RegisterUserView import RegisterUserView
from app.views.RegisterAuditorView import RegisterAuditorView
from app.views.RequirementView import RequirementListView, AddRequirementView, \
    RequirementUpdateView, delete_requirement, RequirementView

from app.views.ShowcaseRequerimentView import requeriment_detail, requirement_showcase_view

from app.views.ChangePasswordView import ChangePasswordView

from app.views.DonatorRequerimentView import  DonatorRequerimentView, DonatorRequerimentViewAnonymous
from app.views.NewItemRequerimentView import NewItemRequerimentView
from app.views.ShowcaseNewItemView import new_item_detail, new_item_showcase_view


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
    url(r'^register-auditor/$', RegisterAuditorView.as_view(), name='register_auditor'),
    url(r'^submit-contact', submit_message, name='submit_contact'),
    url(r'^post/(?P<slug>[^\.]+)', view_post, name='view_post'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^account/logout/$', LogoutView.as_view(), name='auth_logout'),

    url(r'^choose-user/$', ChooseDonation.as_view(), name='choose_user'),
    url(r'^donation-anonymous/$', AnonDonationFormView.as_view(), name='donation_anonymous'),

    url(r'^home/$', PainelView.as_view(), name='painel'),

    url(r'^itens/$', MyItensListView.as_view(), name='list_my_itens'),
    url(r'^donations/$', MyDonationsListView.as_view(), name='list_my_donations'),

    url(r'^object/add/$', RegisterObjectView.as_view(), name='add_object'),
    url(r'^donate-item/$', RegisterObjectView.as_view(template_name='registers/register-item-home.html'), name='add_object_home'),
    url(r'^object/(?P<pk>[0-9]+)/$', ObjectView.as_view(), name='view-object'),
    url(r'^object/(?P<pk>[0-9]+)/edit/$', ObjectUpdateView.as_view(), name='change_object'),
    url(r'^object/(?P<pk>[0-9]+)/delete/$', delete_object, name='delete_object'),

    url(r'^requirements/$', RequirementListView.as_view(), name='list_my_requirements'),
    url(r'^requirements/add/$', AddRequirementView.as_view(), name='add_requirement'),
    url(r'^request-item/$', AddRequirementView.as_view(template_name='registers/register-requirement-home.html'), name='add_requirement_home'),
    url(r'^requirements/(?P<pk>[0-9]+)/$', RequirementView.as_view(), name='view-requirement'),
    url(r'^requirements/(?P<pk>[0-9]+)/edit/$', RequirementUpdateView.as_view(), name='change_requirement'),
    url(r'^requirements/(?P<pk>[0-9]+)/delete/$', delete_requirement, name='delete_requirement'),

    url(r'^institutes/$', InstitutesView.as_view(), name='menu_institutes'),
    url(r'^collect/$', CollectView.as_view(), name='collect_institutes'),
    url(r'^contribute/$', ContributeView.as_view(), name='contribute_institutes'),

    url(r'^profile/(?P<pk>[0-9]+)/$', ProfileUserView.as_view(), name='view-profile'),

    url(r'^audits/$', AuditListView.as_view(), name='list_my_audits'),
    url(r'^audits/add/(?P<pk>[0-9]+)/$', order_item, name='add_audit'),
    url(r'^audits/final/(?P<pk>[0-9]+)/$', final_delivery, name='final_delivery'),
    url(r'^audits/refuse/(?P<pk>[0-9]+)/$', refuse_delivery, name='refuse_delivery'),

    url(r'^audits-user/$', AuditUserListView.as_view(), name='audits_user'),
    url(r'^audits-user/add/(?P<pk>[0-9]+)/$', accept_audit, name='accept_audit'),
    url(r'^audits-user/refuse/(?P<pk>[0-9]+)/$', refuse_audit, name='refuse_audit'),

    url(r'^audits-panel/$', AuditAllListView.as_view(), name='audits_panel'),
    url(r'^audits/(?P<pk>[0-9]+)/$', AuditDetailView.as_view(), name='view-audit'),
    url(r'^audits/(?P<pk>[0-9]+)/edit/$', AuditUpdateView.as_view(), name='change_audit'),
    url(r'^audits/(?P<pk>[0-9]+)/delete/$', delete_audit, name='delete_audit'),

    url(r'^matches/$', MatchListView.as_view(), name='matches'),
    url(r'^matches/(?P<pk>[0-9]+)/edit/$', MatchUpdateView.as_view(), name='change_match'),
    url(r'^matches/(?P<pk>[0-9]+)/delete/$', delete_match, name='delete_match'),

    url(r'^orders/$', OrderListView.as_view(), name='orders'),
    url(r'^orders/(?P<pk>[0-9]+)/edit/$', OrderUpdateView.as_view(), name='change_order'),
    url(r'^orders/(?P<pk>[0-9]+)/delete/$', delete_order, name='delete_order'),

    url(r'^itens/$', DonationListView.as_view(), name='items'),
    url(r'^itens/(?P<pk>[0-9]+)/edit/$', DonationUpdateView.as_view(), name='change_item'),
    url(r'^itens/(?P<pk>[0-9]+)/delete/$', delete_donation, name='delete_item'),

    url(r'^audits-panel/home/$', HomeAuditView.as_view(), name='audit-home'),

    url(r'^notifications/$', NotificationListView.as_view(), name='list_my_notifications'),
    url(r'^notifications/add/(?P<pk>[0-9]+)/$', accept_notification, name='accept_notification'),
    url(r'^notifications/refuse/(?P<pk>[0-9]+)/$', refuse_notification, name='refuse_notification'),
    url(r'^account/(?P<pk>[0-9]+)/edit-donator/$', DonatorUpdateView.as_view(), name='update_donator'),
    url(r'^account/(?P<pk>[0-9]+)/edit-institute/$', InstituteUpdateView.as_view(), name='update_institute'),

    url(r'^requeriments/$', requirement_showcase_view, name='list_showcase'),
    url(r'^requeriments/(?P<requeriment_id>\d+)/$', requeriment_detail, name='detail'),
    url(r'^requeriments/(?P<requeriment_id>\d+)/donationrequeriment/None',
        DonatorRequerimentViewAnonymous.as_view(), name='donation_requeriment_1'),
    url(r'^requeriments/(?P<requeriment_id>\d+)/donationrequeriment/(?P<pk>[0-9]+)/$',
        DonatorRequerimentView.as_view(), name='donation_requeriment'),
    url(r'^new-items/$', new_item_showcase_view, name='list_new_item'),
    url(r'^new-items/(?P<new_item_id>\d+)/$', new_item_detail, name='detail_item'),
    url(r'^new-items/(?P<item_id>\d+)/new-requeriment/$', NewItemRequerimentView.as_view(), name='requerimentnewitem'),
    url(r'^account/(?P<pk>[0-9]+)/change-password/$', ChangePasswordView.as_view(), name='change_password'),

]