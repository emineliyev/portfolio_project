from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from account.forms import LoginForm


class LoginView(View):
    template_name = 'account/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboards:business-plan')
        return render(request, self.template_name, {'form': form})
