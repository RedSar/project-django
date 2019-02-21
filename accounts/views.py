from django.shortcuts import render, redirect


def login(req):
    context = {}
    return render(req, 'accounts/login.html', context)


def register(req):
    context = {}
    return render(req, 'accounts/register.html', context)


def logout(req):
    context = {}
    return redirect('index')


def dashboard(req):
    context = {}
    return render(req, 'accounts/dashboard.html', context)
