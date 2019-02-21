from django.shortcuts import render, redirect
from django.contrib import messages


def login(req):
    if req.method == 'POST':
        messages.success(req, 'You are successfuly connected !')

    return render(req, 'accounts/login.html')


def register(req):
    if req.method == 'POST':
        messages.error(req, 'An error occurs !!')
        messages.info(req, 'this is an info alert')
        messages.warning(req, 'this is warning alert')
        messages.success(req, 'this is success alert')

        return redirect('register')

    return render(req, 'accounts/register.html', )


def logout(req):
    context = {}
    return redirect('index')


def dashboard(req):
    context = {}
    return render(req, 'accounts/dashboard.html', context)
