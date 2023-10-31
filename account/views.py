from django.contrib import auth, messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView
from account.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, ChangePasswordForm
from account.models import User


class UserView(ListView):
    model = User
    template_name = 'account/user-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserView, self).get_context_data()
        context['user_lists'] = User.objects.all().order_by('username')
        return context


def user_delete(request, user_id):
    user = User.objects.get(id=user_id)
    try:
        user.delete()
        messages.success(request, 'İstifadəçi uğurla silindi!')

    except ProtectedError:
        messages.error(request, 'Xəta baş verdi!')
    return redirect('accounts:user-list')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('dashboards:index'))
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Siz istifadəçini uğurla əlavə etdiniz!')
            return HttpResponseRedirect(reverse('accounts:user-list'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'account/registration.html', context=context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        password_form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            if 'old_password' in request.POST:
                if request.POST['old_password']:
                    if password_form.is_valid():
                        password_form.save()
                        update_session_auth_hash(request, password_form.user)
                        messages.success(request, 'Məlumatlar üğürla yeniləndi!')
            return HttpResponseRedirect(reverse('accounts:profile'))
        else:
            if not password_form.user.check_password(request.POST['old_password']):
                password_form.add_error('old_password', 'Неверный старый пароль')
    else:
        form = UserProfileForm(instance=request.user)
        password_form = ChangePasswordForm(request.user)

    context = {
        'form': form,
        'password_form': password_form,
    }
    return render(request, 'account/profile.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')
