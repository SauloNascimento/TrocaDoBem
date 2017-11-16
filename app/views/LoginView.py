from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic import RedirectView

from app.forms import FormLogin

__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class LoginView(FormView):
    """
    Displays the login form.
    """
    template_name = 'login.html'
    form_class = FormLogin
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        user = authenticate(**data)
        print(user)
        if user is not None:
            login(self.request, user)
        else:
            return self.form_invalid(form)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Nenhum usuário encontrado')
        return super(LoginView, self).form_invalid(form)


class LogoutView(RedirectView):
    url = '/'
    permanent = False

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get(request, *args, **kwargs)

#
# from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.utils.decorators import method_decorator
# from django.utils.http import is_safe_url
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.debug import sensitive_post_parameters
# from django.views.generic import FormView, RedirectView
#
#
# class LoginView(FormView):
#     """
#     Provides the ability to login as a user with a username and password
#     """
#     success_url = '/'
#     form_class = AuthenticationForm
#     redirect_field_name = REDIRECT_FIELD_NAME
#
#     @method_decorator(sensitive_post_parameters('password'))
#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):
#         # Sets a test cookie to make sure the user has cookies enabled
#         request.session.set_test_cookie()
#
#         return super(LoginView, self).dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         auth_login(self.request, form.get_user())
#
#         # If the test cookie worked, go ahead and
#         # delete it since its no longer needed
#         if self.request.session.test_cookie_worked():
#             self.request.session.delete_test_cookie()
#
#         return super(LoginView, self).form_valid(form)
#
#     def get_success_url(self):
#         redirect_to = self.request.REQUEST.get(self.redirect_field_name)
#         if not is_safe_url(url=redirect_to, host=self.request.get_host()):
#             redirect_to = self.success_url
#         return redirect_to
#
#
# class LogoutView(RedirectView):
#     """
#     Provides users the ability to logout
#     """
#     url = '/'
#
#     def get(self, request, *args, **kwargs):
#         request.session.clear()
#         auth_logout(request)
#         return super(LogoutView, self).get(request, *args, **kwargs)
