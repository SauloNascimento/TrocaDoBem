from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import FormView

from app.forms import FormRegister
from app.models import CommonUser

__author__ = "Raphaeldobu"
__copyright__ = "Copyright 2017, LES-UFCG"


class RegisterUserView(FormView):
    """
    Displays the login form.
    """
    template_name = 'registers/register-user.html'
    form_class = FormRegister
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print("ta validoo")
            return self.form_valid(form)
        else:
            print("ta invalidoo")
            return self.form_invalid(form)

    def form_valid(self, form):
        data = form.cleaned_data
        last_name = data['last_name']
        password = data['password']
        first_name = data['first_name']
        birth_date = data['birth_date']
        email = data['email']
        username = data['username']
        if username and password:
            print("teeem username e password")
            new_user = User(username=username, password=password, first_name=first_name, last_name=last_name,
                            email=email, is_staff=True, is_active=True)
            new_user.save()
            new_common_user = CommonUser(user=new_user, birth_date=birth_date)
            new_common_user.save()
            messages.success(self.request, 'Novo usuário cadastrado com sucesso.')
        else:
            print("nao tem username e password")
            print("Username: " + username)
            print("Password:" + password)
            return self.form_invalid(form)
        return super(RegisterUserView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Usuário não foi cadastrado.')
        return super(RegisterUserView, self).form_invalid(form)
