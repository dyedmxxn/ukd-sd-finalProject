from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout


def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


def user_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')