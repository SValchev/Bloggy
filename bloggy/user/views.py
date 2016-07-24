from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.contrib.auth import login, logout

from .forms import LoginForm


class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm

    def form_is_valid(self, form):
        username = form.get_username()
        password = form.get_password()

        try:
            user = authenticate(username, password)
        except DoesNotExist:
            context = {'error': u'Invalid user/password',
                   'form': self.get_form()}
            return self.render_to_response(context)
        login(self.request, user)
        return super(LoginView, self).form_is_valid(form)

    def get_success_url(self):
        return reverse('post:index')



def logout_view(request):
    logout(request)
    return redirect(reverse('post:index'))
