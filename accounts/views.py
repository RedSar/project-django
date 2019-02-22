from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User


def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(req, user)
            messages.success(req, 'You are Logged in successfully!')
            return redirect('index')
        else:
            messages.error(req, 'The given credentials ar invalid !')

            return redirect('login')

    return render(req, 'accounts/login.html')


def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(req, 'this username is taken !')
            elif User.objects.filter(email=email).exists():
                messages.error(req, 'this email is being used !')
            else:
                # we're good to go and register the user:
                user = User.objects.create_user(username=username,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                password=password,
                                                )
                user.save()
                messages.success(
                    req, 'You are now successfuly registred and can log in')
                return redirect('login')

        else:
            messages.error(req, 'Passwords do not match !')

        return redirect('register')

    return render(req, 'accounts/register.html', )


def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        messages.success(req, 'You are now loggoed out!')
        return redirect('index')


def dashboard(req):
    context = {}
    return render(req, 'accounts/dashboard.html', context)
